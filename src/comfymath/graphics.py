from abc import ABC, abstractmethod
from typing import Any, Mapping, Sequence, Tuple


SDXL_SUPPORTED_RESOLUTIONS = [
    (1024, 1024, 1.0),
    (1152, 896, 1.2857142857142858),
    (896, 1152, 0.7777777777777778),
    (1216, 832, 1.4615384615384615),
    (832, 1216, 0.6842105263157895),
    (1344, 768, 1.75),
    (768, 1344, 0.5714285714285714),
    (1536, 640, 2.4),
    (640, 1536, 0.4166666666666667),
]

SDXL_EXTENDED_RESOLUTIONS = [
    (512, 2048, 0.25),
    (512, 1984, 0.26),
    (512, 1920, 0.27),
    (512, 1856, 0.28),
    (576, 1792, 0.32),
    (576, 1728, 0.33),
    (576, 1664, 0.35),
    (640, 1600, 0.4),
    (640, 1536, 0.42),
    (704, 1472, 0.48),
    (704, 1408, 0.5),
    (704, 1344, 0.52),
    (768, 1344, 0.57),
    (768, 1280, 0.6),
    (832, 1216, 0.68),
    (832, 1152, 0.72),
    (896, 1152, 0.78),
    (896, 1088, 0.82),
    (960, 1088, 0.88),
    (960, 1024, 0.94),
    (1024, 1024, 1.0),
    (1024, 960, 1.8),
    (1088, 960, 1.14),
    (1088, 896, 1.22),
    (1152, 896, 1.30),
    (1152, 832, 1.39),
    (1216, 832, 1.47),
    (1280, 768, 1.68),
    (1344, 768, 1.76),
    (1408, 704, 2.0),
    (1472, 704, 2.10),
    (1536, 640, 2.4),
    (1600, 640, 2.5),
    (1664, 576, 2.90),
    (1728, 576, 3.0),
    (1792, 576, 3.12),
    (1856, 512, 3.63),
    (1920, 512, 3.76),
    (1984, 512, 3.89),
    (2048, 512, 4.0),
]


class Resolution(ABC):
    @classmethod
    @abstractmethod
    def resolutions(cls) -> Sequence[Tuple[int, int, float]]: ...

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {
            "required": {
                "resolution": ([f"{res[0]}x{res[1]}" for res in cls.resolutions()],)
            }
        }

    RETURN_TYPES = ("INT", "INT")
    RETURN_NAMES = ("width", "height")
    FUNCTION = "op"
    CATEGORY = "math/graphics"

    def op(self, resolution: str) -> tuple[int, int]:
        width, height = resolution.split("x")
        return (int(width), int(height))


class NearestResolution(ABC):
    @classmethod
    @abstractmethod
    def resolutions(cls) -> Sequence[Tuple[int, int, float]]: ...

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {"required": {"image": ("IMAGE",)}}

    RETURN_TYPES = ("INT", "INT")
    RETURN_NAMES = ("width", "height")
    FUNCTION = "op"
    CATEGORY = "math/graphics"

    def op(self, image) -> tuple[int, int]:
        image_width = image.size()[2]
        image_height = image.size()[1]
        print(f"Input image resolution: {image_width}x{image_height}")
        image_ratio = image_width / image_height
        differences = [
            (abs(image_ratio - resolution[2]), resolution)
            for resolution in self.resolutions()
        ]
        smallest = None
        for difference in differences:
            if smallest is None:
                smallest = difference
            else:
                if difference[0] < smallest[0]:
                    smallest = difference
        if smallest is not None:
            width = smallest[1][0]
            height = smallest[1][1]
        else:
            width = 1024
            height = 1024
        print(f"Selected resolution: {width}x{height}")
        return (width, height)


class SDXLResolution(Resolution):
    @classmethod
    def resolutions(cls):
        return SDXL_SUPPORTED_RESOLUTIONS


class SDXLExtendedResolution(Resolution):
    @classmethod
    def resolutions(cls):
        return SDXL_EXTENDED_RESOLUTIONS


class NearestSDXLResolution(NearestResolution):
    @classmethod
    def resolutions(cls):
        return SDXL_SUPPORTED_RESOLUTIONS


class NearestSDXLExtendedResolution(NearestResolution):
    @classmethod
    def resolutions(cls):
        return SDXL_EXTENDED_RESOLUTIONS


NODE_CLASS_MAPPINGS = {
    "CM_SDXLResolution": SDXLResolution,
    "CM_NearestSDXLResolution": NearestSDXLResolution,
    "CM_SDXLExtendedResolution": SDXLExtendedResolution,
    "CM_NearestSDXLExtendedResolution": NearestSDXLExtendedResolution,
}
