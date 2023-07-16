import numpy

from abc import ABC, abstractmethod
from typing import Any, Mapping, TypeAlias

Vec2: TypeAlias = tuple[float, float]
VEC2_ZERO = (0.0, 0.0)


def _vec2_from_numpy(a: numpy.ndarray) -> Vec2:
    return (
        float(a[0]),
        float(a[1]),
    )


class Vec2UnaryOperator(ABC):
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {"required": {"a": ("VEC2", {"default": VEC2_ZERO})}}

    RETURN_TYPES = ("VEC2",)
    FUNCTION = "op"

    def op(self, a: Vec2) -> tuple[Vec2]:
        return (_vec2_from_numpy(self.op_numpy(numpy.array(a))),)

    @abstractmethod
    def op_numpy(self, a: numpy.ndarray) -> numpy.ndarray:
        pass


class Vec2BinaryOperator(ABC):
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {
            "required": {
                "a": ("VEC2", {"default": VEC2_ZERO}),
                "b": ("VEC2", {"default": VEC2_ZERO}),
            }
        }

    RETURN_TYPES = ("VEC2",)
    FUNCTION = "op"

    def op(self, a: Vec2, b: Vec2) -> tuple[Vec2]:
        return (_vec2_from_numpy(self.op_numpy(numpy.array(a), numpy.array(b))),)

    @abstractmethod
    def op_numpy(self, a: numpy.ndarray, b: numpy.ndarray) -> numpy.ndarray:
        pass


class Vec2UnaryQuery(ABC):
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {"required": {"a": ("VEC2", {"default": VEC2_ZERO})}}

    RETURN_TYPES = ("INT",)
    FUNCTION = "op"

    def op(self, a: Vec2) -> tuple[int]:
        return (self.op_numpy(numpy.array(a)),)

    @abstractmethod
    def op_numpy(self, a: numpy.ndarray) -> int:
        pass


class Vec2BinaryQuery(ABC):
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {
            "required": {
                "a": ("VEC2", {"default": VEC2_ZERO}),
                "b": ("VEC2", {"default": VEC2_ZERO}),
            }
        }

    RETURN_TYPES = ("INT",)
    FUNCTION = "op"

    def op(self, a: Vec2, b: Vec2) -> tuple[int]:
        return (self.op_numpy(numpy.array(a), numpy.array(b)),)

    @abstractmethod
    def op_numpy(self, a: numpy.ndarray, b: numpy.ndarray) -> int:
        pass


class Vec2ToScalarUnary(ABC):
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {"required": {"a": ("VEC2", {"default": VEC2_ZERO})}}

    RETURN_TYPES = ("FLOAT",)
    FUNCTION = "op"

    def op(self, a: Vec2) -> tuple[float]:
        return (self.op_numpy(numpy.array(a)),)

    @abstractmethod
    def op_numpy(self, a: numpy.ndarray) -> float:
        pass


class Vec2ToScalarBinary(ABC):
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {
            "required": {
                "a": ("VEC2", {"default": VEC2_ZERO}),
                "b": ("VEC2", {"default": VEC2_ZERO}),
            }
        }

    RETURN_TYPES = ("FLOAT",)
    FUNCTION = "op"

    def op(self, a: Vec2, b: Vec2) -> tuple[float]:
        return (self.op_numpy(numpy.array(a), numpy.array(b)),)

    @abstractmethod
    def op_numpy(self, a: numpy.ndarray, b: numpy.ndarray) -> float:
        pass


class Vec2ScalarOperation(ABC):
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {
            "required": {
                "a": ("VEC2", {"default": VEC2_ZERO}),
                "b": ("FLOAT", {"default": 0.0}),
            }
        }

    RETURN_TYPES = ("VEC2",)
    FUNCTION = "op"

    def op(self, a: Vec2, b: float) -> tuple[Vec2]:
        return (_vec2_from_numpy(self.op_numpy(numpy.array(a), b)),)

    @abstractmethod
    def op_numpy(self, a: numpy.ndarray, b: float) -> numpy.ndarray:
        pass


class Vec2Add(Vec2BinaryOperator):
    def op_numpy(self, a: numpy.ndarray, b: numpy.ndarray) -> numpy.ndarray:
        return a + b

    CATEGORY = "math/vec2"


class Vec2Sub(Vec2BinaryOperator):
    def op_numpy(self, a: numpy.ndarray, b: numpy.ndarray) -> numpy.ndarray:
        return a - b

    CATEGORY = "math/vec2"


class Vec2Dot(Vec2ToScalarBinary):
    def op_numpy(self, a: numpy.ndarray, b: numpy.ndarray) -> float:
        return a.dot(b).astype(float)

    CATEGORY = "math/vec2"


class Vec2Cross(Vec2BinaryOperator):
    def op_numpy(self, a: numpy.ndarray, b: numpy.ndarray) -> numpy.ndarray:
        return numpy.cross(a, b)

    CATEGORY = "math/vec2"


class Vec2Eq(Vec2BinaryQuery):
    def op_numpy(self, a: numpy.ndarray, b: numpy.ndarray) -> int:
        return int(a == b)

    CATEGORY = "math/vec2"


class Vec2Ne(Vec2BinaryQuery):
    def op_numpy(self, a: numpy.ndarray, b: numpy.ndarray) -> int:
        return int(a != b)

    CATEGORY = "math/vec2"


class Vec2Neg(Vec2UnaryOperator):
    def op_numpy(self, a: numpy.ndarray) -> numpy.ndarray:
        return -a

    CATEGORY = "math/vec2"


class Vec2Norm(Vec2ToScalarUnary):
    def op_numpy(self, a: numpy.ndarray) -> float:
        return numpy.linalg.norm(a).astype(float)

    CATEGORY = "math/vec2"


class Vec2Normalize(Vec2UnaryOperator):
    def op_numpy(self, a: numpy.ndarray) -> numpy.ndarray:
        return a / numpy.linalg.norm(a)

    CATEGORY = "math/vec2"


class Vec2Distance(Vec2ToScalarBinary):
    def op_numpy(self, a: numpy.ndarray, b: numpy.ndarray) -> float:
        return numpy.linalg.norm(a - b).astype(float)

    CATEGORY = "math/vec2"


class Vec2ScalarMul(Vec2ScalarOperation):
    def op_numpy(self, a: numpy.ndarray, b: float) -> numpy.ndarray:
        return a * b

    CATEGORY = "math/vec2"


NODE_CLASS_MAPPINGS = {
    "Vec2Add": Vec2Add,
    "Vec2Sub": Vec2Sub,
    "Vec2Dot": Vec2Dot,
    "Vec2Cross": Vec2Cross,
    "Vec2Eq": Vec2Eq,
    "Vec2Ne": Vec2Ne,
    "Vec2Neg": Vec2Neg,
    "Vec2Norm": Vec2Norm,
    "Vec2Normalize": Vec2Normalize,
    "Vec2Distance": Vec2Distance,
    "Vec2ScalarMul": Vec2ScalarMul,
}
