import numpy

from abc import ABC, abstractmethod
from typing import Any, Mapping, TypeAlias

Vec3: TypeAlias = tuple[float, float, float]
VEC3_ZERO = (0.0, 0.0, 0.0)


def _vec3_from_numpy(a: numpy.ndarray) -> Vec3:
    return (
        float(a[0]),
        float(a[1]),
        float(a[2]),
    )


class Vec3UnaryOperator(ABC):
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {"required": {"a": ("VEC3", {"default": VEC3_ZERO})}}

    RETURN_TYPES = ("VEC3",)
    FUNCTION = "op"

    def op(self, a: Vec3) -> tuple[Vec3]:
        return (_vec3_from_numpy(self.op_numpy(numpy.array(a))),)

    @abstractmethod
    def op_numpy(self, a: numpy.ndarray) -> numpy.ndarray:
        pass


class Vec3BinaryOperator(ABC):
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {
            "required": {
                "a": ("VEC3", {"default": VEC3_ZERO}),
                "b": ("VEC3", {"default": VEC3_ZERO}),
            }
        }

    RETURN_TYPES = ("VEC3",)
    FUNCTION = "op"

    def op(self, a: Vec3, b: Vec3) -> tuple[Vec3]:
        return (_vec3_from_numpy(self.op_numpy(numpy.array(a), numpy.array(b))),)

    @abstractmethod
    def op_numpy(self, a: numpy.ndarray, b: numpy.ndarray) -> numpy.ndarray:
        pass


class Vec3UnaryQuery(ABC):
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {"required": {"a": ("VEC3", {"default": VEC3_ZERO})}}

    RETURN_TYPES = ("INT",)
    FUNCTION = "op"

    def op(self, a: Vec3) -> tuple[int]:
        return (self.op_numpy(numpy.array(a)),)

    @abstractmethod
    def op_numpy(self, a: numpy.ndarray) -> int:
        pass


class Vec3BinaryQuery(ABC):
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {
            "required": {
                "a": ("VEC3", {"default": VEC3_ZERO}),
                "b": ("VEC3", {"default": VEC3_ZERO}),
            }
        }

    RETURN_TYPES = ("INT",)
    FUNCTION = "op"

    def op(self, a: Vec3, b: Vec3) -> tuple[int]:
        return (self.op_numpy(numpy.array(a), numpy.array(b)),)

    @abstractmethod
    def op_numpy(self, a: numpy.ndarray, b: numpy.ndarray) -> int:
        pass


class Vec3ToScalarUnary(ABC):
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {"required": {"a": ("VEC2", {"default": VEC3_ZERO})}}

    RETURN_TYPES = ("FLOAT",)
    FUNCTION = "op"

    def op(self, a: Vec3) -> tuple[float]:
        return (self.op_numpy(numpy.array(a)),)

    @abstractmethod
    def op_numpy(self, a: numpy.ndarray) -> float:
        pass


class Vec3ToScalarBinary(ABC):
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {
            "required": {
                "a": ("VEC2", {"default": VEC3_ZERO}),
                "b": ("VEC2", {"default": VEC3_ZERO}),
            }
        }

    RETURN_TYPES = ("FLOAT",)
    FUNCTION = "op"

    def op(self, a: Vec3, b: Vec3) -> tuple[float]:
        return (self.op_numpy(numpy.array(a), numpy.array(b)),)

    @abstractmethod
    def op_numpy(self, a: numpy.ndarray, b: numpy.ndarray) -> float:
        pass


class Vec3ScalarOperation(ABC):
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {
            "required": {
                "a": ("VEC3", {"default": VEC3_ZERO}),
                "b": ("FLOAT", {"default": 0.0}),
            }
        }

    RETURN_TYPES = ("VEC3",)
    FUNCTION = "op"

    def op(self, a: Vec3, b: float) -> tuple[Vec3]:
        return (_vec3_from_numpy(self.op_numpy(numpy.array(a), b)),)

    @abstractmethod
    def op_numpy(self, a: numpy.ndarray, b: float) -> numpy.ndarray:
        pass


class Vec3Add(Vec3BinaryOperator):
    def op_numpy(self, a: numpy.ndarray, b: numpy.ndarray) -> numpy.ndarray:
        return a + b

    CATEGORY = "math/vec3"


class Vec3Sub(Vec3BinaryOperator):
    def op_numpy(self, a: numpy.ndarray, b: numpy.ndarray) -> numpy.ndarray:
        return a - b

    CATEGORY = "math/vec3"


class Vec3Dot(Vec3ToScalarBinary):
    def op_numpy(self, a: numpy.ndarray, b: numpy.ndarray) -> float:
        return a.dot(b).astype(float)

    CATEGORY = "math/vec3"


class Vec3Cross(Vec3BinaryOperator):
    def op_numpy(self, a: numpy.ndarray, b: numpy.ndarray) -> numpy.ndarray:
        return numpy.cross(a, b)

    CATEGORY = "math/vec3"


class Vec3Eq(Vec3BinaryQuery):
    def op_numpy(self, a: numpy.ndarray, b: numpy.ndarray) -> int:
        return int(a == b)

    CATEGORY = "math/vec3"


class Vec3Ne(Vec3BinaryQuery):
    def op_numpy(self, a: numpy.ndarray, b: numpy.ndarray) -> int:
        return int(a != b)

    CATEGORY = "math/vec3"


class Vec3Neg(Vec3UnaryOperator):
    def op_numpy(self, a: numpy.ndarray) -> numpy.ndarray:
        return -a

    CATEGORY = "math/vec3"


class Vec3Norm(Vec3ToScalarUnary):
    def op_numpy(self, a: numpy.ndarray) -> float:
        return numpy.linalg.norm(a).astype(float)

    CATEGORY = "math/vec3"


class Vec3Normalize(Vec3UnaryOperator):
    def op_numpy(self, a: numpy.ndarray) -> numpy.ndarray:
        return a / numpy.linalg.norm(a)

    CATEGORY = "math/vec3"


class Vec3Distance(Vec3ToScalarBinary):
    def op_numpy(self, a: numpy.ndarray, b: numpy.ndarray) -> float:
        return numpy.linalg.norm(a - b).astype(float)

    CATEGORY = "math/vec3"


class Vec3ScalarMul(Vec3ScalarOperation):
    def op_numpy(self, a: numpy.ndarray, b: float) -> numpy.ndarray:
        return a * b

    CATEGORY = "math/vec3"


NODE_CLASS_MAPPINGS = {
    "Vec3Add": Vec3Add,
    "Vec3Sub": Vec3Sub,
    "Vec3Dot": Vec3Dot,
    "Vec3Cross": Vec3Cross,
    "Vec3Eq": Vec3Eq,
    "Vec3Ne": Vec3Ne,
    "Vec3Neg": Vec3Neg,
    "Vec3Norm": Vec3Norm,
    "Vec3Normalize": Vec3Normalize,
    "Vec3Distance": Vec3Distance,
    "Vec3ScalarMul": Vec3ScalarMul,
}
