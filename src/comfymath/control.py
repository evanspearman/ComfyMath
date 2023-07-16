from typing import Any, Mapping, Callable


def _pascalcase(input_str: str) -> str:
    return input_str.lower().title().replace("_", "")


def _get_input_types_method(input_type: str) -> Callable[[], Mapping[str, Any]]:
    input_type_tuple: tuple = (input_type,)
    if input_type == "INT":
        input_type_tuple = ("INT", {"default": 0})
    if input_type == "FLOAT":
        input_type_tuple = ("FLOAT", {"default": 0.0})
    if input_type == "STRING":
        input_type_tuple = ("STRING", {"default": ""})
    return lambda: {
        "required": {
            "condition": ("INT", {"default": 0}),
            "then": input_type_tuple,
            "else_": input_type_tuple,
        }
    }


def _op_if(self, condition: int, then: Any, else_: Any) -> Any:
    if condition != 0:
        return (then,)
    else:
        return (else_,)


def _make_if_node_class(input_type: str, category: str) -> type:
    name = f"{_pascalcase(input_type)}If"

    class_dict = {
        "INPUT_TYPES": _get_input_types_method(input_type),
        "RETURN_TYPES": (input_type,),
        "FUNCTION": "op",
        "CATEGORY": category,
        "op": _op_if,
    }

    return type(name, (), class_dict)


_TYPES = {
    "INT": "base",
    "FLOAT": "base",
    "STRING": "base",
    "CONDITIONING": "base",
    "IMAGE": "base",
    "LATENT": "base",
    "MODEL": "base",
    "CLIP": "base",
    "VAE": "base",
    "CLIP_VISION": "base",
    "CONTROL_NET": "base",
    "CLIP_VISION_OUTPUT": "base",
    "STYLE_MODEL": "base",
    "GLIGEN": "base",
    "MASK": "base",
    # Comfy Math
    "VEC2": "math",
    "VEC3": "math",
    "VEC4": "math",
    # Was Node Suite
    "CROP_DATA": "was",
    "LIST": "was",
    "MIDAS_MODEL": "was",
    "SEED": "was",
    "DICT": "was",
    "NUMBER": "was",
    "BLIP_MODEL": "was",
    "CLIPSEG_MODEL": "was",
    "LANG_SAM_MODEL": "was",
    "SAM_MODEL": "was",
    "SAM_PARAMETERS": "was",
    "IMAGE_BOUNDS": "was",
    "UPSCALE_MODEL": "was",
    # Impact Pack
    "ONNX_DETECTOR": "impact",
    "BBOX_DETECTOR": "impact",
    "SEGM_DETECTOR": "impact",
    "SEGS": "impact",
    "KSAMPLER": "impact",
    "KSAMPLER_ADVANCED": "impact",
    "REGIONAL_PROMPTS": "impact",
    "DETAILER_PIPE": "impact",
    "PK_HOOK": "impact",
    "UPSCALER": "impact",
}


IF_CLASS_MAPPINGS = {
    f"{_pascalcase(type_name)}If": _make_if_node_class(
        type_name, f"math/control/if/{category}"
    )
    for type_name, category in _TYPES.items()
}


NODE_CLASS_MAPPINGS = {
    **IF_CLASS_MAPPINGS,
}
