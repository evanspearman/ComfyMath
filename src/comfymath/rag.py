import re

from typing import Any, Optional, Protocol, TypeAlias
from pathlib import Path

import numpy
import torch

from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, CollectionStatus, PointStruct
from uuid import uuid4
from torch import Tensor
from tqdm import tqdm
from PIL import Image, ImageOps

_qdrant_connections: dict[str, QdrantClient] = {}


def _get_qdrant_connection(connection_id: str) -> QdrantClient:
    if connection_id not in _qdrant_connections:
        raise ValueError(f"Connection {connection_id} not found")
    return _qdrant_connections[connection_id]


def _get_unused_qdrant_id(qdrant_connection: QdrantClient, collection: str) -> str:
    while (
        len(
            qdrant_connection.retrieve(
                collection_name=collection, ids=[id := uuid4().hex]
            )
        )
        > 0
    ):
        pass
    return id


def _get_sequence_from_file_path(original_path: Path) -> list[Path]:
    match = SEQUENCE_REGEX.match(original_path.name)
    if match is None:
        return [original_path]
    results = {int(match.group(2)): original_path}
    directory = original_path.parent
    for child_path in directory.iterdir():
        if child_path.is_file():
            child_match = SEQUENCE_REGEX.match(child_path.name)
            if child_match is not None:
                if child_match.group(1) == match.group(1) and child_match.group(
                    3
                ) == match.group(3):
                    results[int(child_match.group(2))] = child_path
    sorted_keys = sorted(results.keys())
    return [results[key] for key in sorted_keys]


def _load_image_to_tensor(path: Path) -> Tensor:
    image = ImageOps.exif_transpose(Image.open(path)).convert("RGB")
    image_array = numpy.array(image).astype(numpy.float32) / 255.0
    return torch.from_numpy(image_array)[None,]


SEQUENCE_REGEX = re.compile(r"^(.*?)(\d+)(\D*)$")


_Conditioning: TypeAlias = list[list[dict[str, Tensor]]]


class _CLIPVisionOutput(Protocol):
    image_embeds: Tensor


class _CLIPVisionModel(Protocol):
    def encode_image(self, Tensor) -> _CLIPVisionOutput:
        pass


class AddStringToDict:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "key": ("STRING", {"default": "", "multiline": False}),
                "value": ("STRING", {"default": "", "multiline": False}),
            },
            "optional": {"input_dict": ("DICT",)},
        }

    RETURN_TYPES = ("DICT",)
    FUNCTION = "op"
    CATEGORY = "math/data_structures"

    def op(
        self, key: str, value: str, input_dict: Optional[dict[str, Any]] = None
    ) -> tuple[dict]:
        output_dict = input_dict.copy() if input_dict else {}
        output_dict[key] = value
        return (output_dict,)


class RetrieveStringFromDict:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "key": ("STRING", {"default": "", "multiline": False}),
                "input_dict": ("DICT",),
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "op"
    CATEGORY = "math/data_structures"

    def op(self, key: str, input_dict: dict[str, Any]) -> tuple[str]:
        value = input_dict[key]
        if not isinstance(value, str):
            raise RuntimeError(f"Value at key {key} is not a string.")
        return (value,)


class StringAtIndex:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "string_list": ("STRING", {"forceInput": True}),
                "index": ("INT", {"default": 0, "min": 0}),
            },
        }

    RETURN_TYPES = ("STRING",)
    INPUT_IS_LIST = True
    FUNCTION = "op"
    CATEGORY = "math/data_structures"

    def op(self, string_list: list[str], index: list[int]) -> tuple[str]:
        return (string_list[index[0]],)


class FloatAtIndex:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "float_list": ("FLOAT", {"forceInput": True}),
                "index": ("INT", {"default": 0, "min": 0}),
            }
        }

    RETURN_TYPES = ("FLOAT",)
    INPUT_IS_LIST = True
    FUNCTION = "op"
    CATEGORY = "math/data_structures"

    def op(self, float_list: list[float], index: list[int]) -> tuple[float]:
        return (float_list[index[0]],)


class LoadImageFromPath:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image_path": ("STRING", {"default": "", "multiline": False}),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image",)
    FUNCTION = "op"
    CATEGORY = "math/image_files"

    def op(self, image_path: str) -> tuple[Tensor]:
        return (_load_image_to_tensor(Path(image_path)),)


class GetImageSequence:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image_sequence_path": ("STRING", {"default": "", "multiline": False}),
            }
        }

    RETURN_TYPES = ("STRING", "INT")
    RETURN_NAMES = ("image_paths", "sequence_length")
    OUTPUT_IS_LIST = (True, False)
    FUNCTION = "op"
    CATEGORY = "math/image_files"

    def op(self, image_sequence_path: str) -> tuple[list[str], int]:
        file_sequence = _get_sequence_from_file_path(Path(image_sequence_path))
        return (
            [str(path) for path in file_sequence],
            len(file_sequence),
        )


class QdrantConnectionFromFile:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "path": ("STRING", {"default": "", "multiline": False}),
            },
        }

    RETURN_TYPES = ("QDRANT_CONNECTION",)
    FUNCTION = "op"
    CATEGORY = "math/vectordb/qdrant"

    def op(self, path: str) -> tuple[str]:
        client = QdrantClient(path=path)
        while (id := uuid4().hex) in _qdrant_connections:
            pass
        _qdrant_connections[id] = client
        return (id,)


class QdrantCollection:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "connection": ("QDRANT_CONNECTION",),
                "collection_name": ("STRING", {"default": "", "multiline": False}),
            },
            "optional": {
                "vector_size": ("INT", {"default": 1280, "min": 0}),
                "distance": (["Cosine", "Euclid", "Dot"],),
            },
        }

    RETURN_TYPES = ("QDRANT_COLLECTION",)
    FUNCTION = "op"
    CATEGORY = "math/vectordb/qdrant"

    def op(
        self,
        connection: str,
        collection_name: str,
        vector_size: Optional[int],
        distance: Optional[str],
    ) -> tuple[dict[str, str]]:
        qdrant_connection = _get_qdrant_connection(connection)
        try:
            connection_info = qdrant_connection.get_collection(
                collection_name=collection_name
            )
            if connection_info.status != CollectionStatus.GREEN:
                raise RuntimeError(f"Collection {collection_name} is not available.")
        except ValueError:
            real_vector_size = vector_size if vector_size is not None else 512
            real_distance = Distance.COSINE if distance is None else distance
            match real_distance:
                case "Cosine":
                    real_distance_value = Distance.COSINE
                case "Euclid":
                    real_distance_value = Distance.EUCLID
                case "Dot":
                    real_distance_value = Distance.DOT
                case _:
                    raise ValueError(f"Unknown distance {distance}.")
            qdrant_connection.recreate_collection(
                collection_name=collection_name,
                vectors_config=VectorParams(
                    size=real_vector_size, distance=real_distance_value
                ),
            )
        return ({"connection": connection, "name": collection_name},)


class CLIPVisionOutputToQdrantVector:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "clip_vision_output": ("CLIP_VISION_OUTPUT",),
            },
        }

    RETURN_TYPES = ("QDRANT_VECTOR",)
    FUNCTION = "op"
    CATEGORY = "math/vectordb/qdrant"

    def op(
        self,
        clip_vision_output: _CLIPVisionOutput,
    ) -> tuple[list[float]]:
        return (clip_vision_output.image_embeds.flatten().tolist(),)


class ConditioningToQdrantVector:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "conditioning": ("CONDITIONING",),
            },
        }

    RETURN_TYPES = ("QDRANT_VECTOR",)
    FUNCTION = "op"
    CATEGORY = "math/vectordb/qdrant"

    def op(
        self,
        conditioning: _Conditioning,
    ) -> tuple[list[float]]:
        return (conditioning[0][1]["pooled_output"].flatten().tolist(),)


class QdrantInsertVector:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "collection": ("QDRANT_COLLECTION",),
                "vector": ("QDRANT_VECTOR",),
            },
            "optional": {"payload": ("DICT",)},
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("id",)
    OUTPUT_NODE = True
    FUNCTION = "op"
    CATEGORY = "math/vectordb/qdrant"

    def op(
        self,
        collection: dict[str, str],
        vector: list[float],
        payload: Optional[dict] = None,
    ) -> tuple[str]:
        qdrant_connection = _get_qdrant_connection(collection["connection"])
        collection_name = collection["name"]
        id = _get_unused_qdrant_id(qdrant_connection, collection_name)

        qdrant_connection.upsert(
            collection_name=collection_name,
            points=[
                PointStruct(
                    id=id,
                    vector=vector,
                    payload=payload,
                )
            ],
        )
        return (id,)


class QdrantRetrievePayloadById:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "collection": ("QDRANT_COLLECTION",),
                "id": ("STRING", {"default": "", "multiline": False}),
            }
        }

    RETURN_TYPES = ("DICT",)
    FUNCTION = "op"
    CATEGORY = "math/vectordb/qdrant"

    def op(self, collection: dict[str, str], id: str) -> tuple[dict[str, Any]]:
        qdrant_connection = _get_qdrant_connection(collection["connection"])
        collection_name = collection["name"]
        result = qdrant_connection.retrieve(
            collection_name=collection_name, ids=[id], with_payload=True
        )
        if result[0].payload is None:
            raise RuntimeError(f"No such id {id} in collection {collection_name}")
        return (result[0].payload,)


class QdrantSearch:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "collection": ("QDRANT_COLLECTION",),
                "query_vector": ("QDRANT_VECTOR",),
                "limit": ("INT", {"default": 1, "min": 1}),
            },
        }

    RETURN_TYPES = ("STRING", "FLOAT")
    RETURN_NAMES = ("ids", "scores")
    OUTPUT_IS_LIST = (True, True)
    FUNCTION = "op"
    CATEGORY = "math/vectordb/qdrant"

    def op(
        self, collection: dict[str, str], query_vector: list[float], limit: int
    ) -> tuple[list[str], list[float]]:
        qdrant_connection = _get_qdrant_connection(collection["connection"])
        collection_name = collection["name"]
        results = qdrant_connection.search(
            collection_name=collection_name, query_vector=query_vector, limit=limit
        )
        return (
            [str(result.id) for result in results],
            [result.score for result in results],
        )


class QdrantInsertImageSequence:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "collection": ("QDRANT_COLLECTION",),
                "clip_vision": ("CLIP_VISION",),
                "image_paths": ("STRING", {"forceInput": True}),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("ids",)
    OUTPUT_IS_LIST = (True,)
    INPUT_IS_LIST = True
    OUTPUT_NODE = True
    FUNCTION = "op"
    CATEGORY = "math/vectordb/qdrant"

    def op(
        self,
        collection: list[dict[str, str]],
        clip_vision: list[_CLIPVisionModel],
        image_paths: list[str],
    ) -> tuple[list[str]]:
        qdrant_connection = _get_qdrant_connection(collection[0]["connection"])
        collection_name = collection[0]["name"]
        clip_vision_model = clip_vision[0]

        ids = []
        for path in tqdm(image_paths, desc="Encoding and upserting images to Qdrant DB"):
            image = _load_image_to_tensor(Path(path))
            image_embedding = (
                clip_vision_model.encode_image(image).image_embeds.flatten().tolist()
            )
            ids.append(id := _get_unused_qdrant_id(qdrant_connection, collection_name))
            qdrant_connection.upsert(
                collection_name=collection_name,
                points=[
                    PointStruct(
                        id=id,
                        vector=image_embedding,
                        payload={"path": path},
                    )
                ],
            )

        return (ids,)


NODE_CLASS_MAPPINGS = {
    "CM_AddStringToDict": AddStringToDict,
    "CM_RetrieveStringFromDict": RetrieveStringFromDict,
    "CM_StringAtIndex": StringAtIndex,
    "CM_FloatAtIndex": FloatAtIndex,
    "CM_LoadImageFromPath": LoadImageFromPath,
    "CM_GetImageSequence": GetImageSequence,
    "CM_QdrantConnectionFromFile": QdrantConnectionFromFile,
    "CM_QdrantCollection": QdrantCollection,
    "CM_CLIPVisionOutputToQdrantVector": CLIPVisionOutputToQdrantVector,
    "CM_ConditioningToQdrantVector": ConditioningToQdrantVector,
    "CM_QdrantInsertVector": QdrantInsertVector,
    "CM_QdrantRetrievePayloadById": QdrantRetrievePayloadById,
    "CM_QdrantSearch": QdrantSearch,
    "CM_QdrantInsertImageSequence": QdrantInsertImageSequence,
}
