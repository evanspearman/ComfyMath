from typing import Any, Mapping

from .vec2 import Vec2, VEC2_ZERO
from .vec3 import Vec3, VEC3_ZERO
from .vec4 import Vec4, VEC4_ZERO


class FloatToInt:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {"required": {"a": ("FLOAT", {"default": 0.0})}}

    RETURN_TYPES = ("INT",)
    FUNCTION = "op"
    CATEGORY = "math/conversion"

    def op(self, a: float) -> tuple[int]:
        return (int(a),)


class IntToFloat:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {"required": {"a": ("INT", {"default": 0})}}

    RETURN_TYPES = ("FLOAT",)
    FUNCTION = "op"
    CATEGORY = "math/conversion"

    def op(self, a: int) -> tuple[float]:
        return (float(a),)


class ComposeVec2:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {
            "required": {
                "x": ("FLOAT", {"default": 0.0}),
                "y": ("FLOAT", {"default": 0.0}),
            }
        }

    RETURN_TYPES = ("VEC2",)
    FUNCTION = "op"
    CATEGORY = "math/conversion"

    def op(self, x: float, y: float) -> tuple[Vec2]:
        return ((x, y),)


class BreakoutVec2:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {"required": {"a": ("VEC2", {"default": VEC2_ZERO})}}

    RETURN_TYPES = ("FLOAT", "FLOAT")
    FUNCTION = "op"
    CATEGORY = "math/conversion"

    def op(self, a: Vec2) -> tuple[float, float]:
        return (a[0], a[1])


class ComposeVec3:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {
            "required": {
                "x": ("FLOAT", {"default": 0.0}),
                "y": ("FLOAT", {"default": 0.0}),
                "z": ("FLOAT", {"default": 0.0}),
            }
        }

    RETURN_TYPES = ("VEC3",)
    FUNCTION = "op"
    CATEGORY = "math/conversion"

    def op(self, x: float, y: float, z: float) -> tuple[Vec3]:
        return ((x, y, z),)


class BreakoutVec3:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {"required": {"a": ("VEC3", {"default": VEC3_ZERO})}}

    RETURN_TYPES = ("FLOAT", "FLOAT", "FLOAT")
    FUNCTION = "op"
    CATEGORY = "math/conversion"

    def op(self, a: Vec3) -> tuple[float, float, float]:
        return (a[0], a[1], a[2])


class ComposeVec4:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {
            "required": {
                "x": ("FLOAT", {"default": 0.0}),
                "y": ("FLOAT", {"default": 0.0}),
                "z": ("FLOAT", {"default": 0.0}),
                "w": ("FLOAT", {"default": 0.0}),
            }
        }

    RETURN_TYPES = ("VEC4",)
    FUNCTION = "op"
    CATEGORY = "math/conversion"

    def op(self, x: float, y: float, z: float, w: float) -> tuple[Vec4]:
        return ((x, y, z, w),)


class BreakoutVec4:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {"required": {"a": ("VEC4", {"default": VEC4_ZERO})}}

    RETURN_TYPES = ("FLOAT", "FLOAT", "FLOAT", "FLOAT")
    FUNCTION = "op"
    CATEGORY = "math/conversion"

    def op(self, a: Vec4) -> tuple[float, float, float, float]:
        return (a[0], a[1], a[2], a[3])


NODE_CLASS_MAPPINGS = {
    "FloatToInt": FloatToInt,
    "IntToFloat": IntToFloat,
    "ComposeVec2": ComposeVec2,
    "ComposeVec3": ComposeVec3,
    "ComposeVec4": ComposeVec4,
    "BreakoutVec2": BreakoutVec2,
    "BreakoutVec3": BreakoutVec3,
    "BreakoutVec4": BreakoutVec4,
}
