import numpy

from abc import ABC, abstractmethod
from typing import Any, Mapping, TypeAlias

Vec4: TypeAlias = tuple[float, float, float, float]
VEC4_ZERO = (0.0, 0.0, 0.0, 0.0)


def _vec4_from_numpy(a: numpy.ndarray) -> Vec4:
    return (
        float(a[0]),
        float(a[1]),
        float(a[2]),
        float(a[3]),
    )


class Vec4UnaryOperator(ABC):
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {"required": {"a": ("VEC4", {"default": VEC4_ZERO})}}

    RETURN_TYPES = ("VEC4",)
    FUNCTION = "op"

    def op(self, a: Vec4) -> Vec4:
        return _vec4_from_numpy(self.op_numpy(numpy.array(a)))

    @abstractmethod
    def op_numpy(self, a: numpy.ndarray) -> numpy.ndarray:
        pass


class Vec4BinaryOperator(ABC):
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {
            "required": {
                "a": ("VEC4", {"default": VEC4_ZERO}),
                "b": ("VEC4", {"default": VEC4_ZERO}),
            }
        }

    RETURN_TYPES = ("VEC4",)
    FUNCTION = "op"

    def op(self, a: Vec4, b: Vec4) -> Vec4:
        return _vec4_from_numpy(self.op_numpy(numpy.array(a), numpy.array(b)))

    @abstractmethod
    def op_numpy(self, a: numpy.ndarray, b: numpy.ndarray) -> numpy.ndarray:
        pass


class Vec4UnaryQuery(ABC):
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {"required": {"a": ("VEC4", {"default": VEC4_ZERO})}}

    RETURN_TYPES = ("BOOL",)
    FUNCTION = "op"

    def op(self, a: Vec4) -> bool:
        return self.op_numpy(numpy.array(a))

    @abstractmethod
    def op_numpy(self, a: numpy.ndarray) -> bool:
        pass


class Vec4BinaryQuery(ABC):
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {
            "required": {
                "a": ("VEC4", {"default": VEC4_ZERO}),
                "b": ("VEC4", {"default": VEC4_ZERO}),
            }
        }

    RETURN_TYPES = ("BOOL",)
    FUNCTION = "op"

    def op(self, a: Vec4, b: Vec4) -> bool:
        return self.op_numpy(numpy.array(a), numpy.array(b))

    @abstractmethod
    def op_numpy(self, a: numpy.ndarray, b: numpy.ndarray) -> bool:
        pass


class Vec4ToScalarUnary(ABC):
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {"required": {"a": ("VEC4", {"default": VEC4_ZERO})}}

    RETURN_TYPES = ("FLOAT",)
    FUNCTION = "op"

    def op(self, a: Vec4) -> float:
        return self.op_numpy(numpy.array(a))

    @abstractmethod
    def op_numpy(self, a: numpy.ndarray) -> float:
        pass


class Vec4ToScalarBinary(ABC):
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {
            "required": {
                "a": ("VEC4", {"default": VEC4_ZERO}),
                "b": ("VEC4", {"default": VEC4_ZERO}),
            }
        }

    RETURN_TYPES = ("FLOAT",)
    FUNCTION = "op"

    def op(self, a: Vec4, b: Vec4) -> float:
        return self.op_numpy(numpy.array(a), numpy.array(b))

    @abstractmethod
    def op_numpy(self, a: numpy.ndarray, b: numpy.ndarray) -> float:
        pass


class Vec4ScalarOperation(ABC):
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {
            "required": {
                "a": ("VEC4", {"default": VEC4_ZERO}),
                "b": ("FLOAT", {"default": 0.0}),
            }
        }

    RETURN_TYPES = ("VEC4",)
    FUNCTION = "op"

    def op(self, a: Vec4, b: float) -> Vec4:
        return _vec4_from_numpy(self.op_numpy(numpy.array(a), b))

    @abstractmethod
    def op_numpy(self, a: numpy.ndarray, b: float) -> numpy.ndarray:
        pass


class Vec4Add(Vec4BinaryOperator):
    def op_numpy(self, a: numpy.ndarray, b: numpy.ndarray) -> numpy.ndarray:
        return a + b

    CATEGORY = "math/vec4"


class Vec4Sub(Vec4BinaryOperator):
    def op_numpy(self, a: numpy.ndarray, b: numpy.ndarray) -> numpy.ndarray:
        return a - b

    CATEGORY = "math/vec4"


class Vec4Dot(Vec4ToScalarBinary):
    def op_numpy(self, a: numpy.ndarray, b: numpy.ndarray) -> float:
        return a.dot(b).astype(float)

    CATEGORY = "math/vec4"


class Vec4Cross(Vec4BinaryOperator):
    def op_numpy(self, a: numpy.ndarray, b: numpy.ndarray) -> numpy.ndarray:
        return numpy.cross(a, b)

    CATEGORY = "math/vec4"


class Vec4Eq(Vec4BinaryQuery):
    def op_numpy(self, a: numpy.ndarray, b: numpy.ndarray) -> bool:
        return a == b

    CATEGORY = "math/vec4"


class Vec4Ne(Vec4BinaryQuery):
    def op_numpy(self, a: numpy.ndarray, b: numpy.ndarray) -> bool:
        return a != b

    CATEGORY = "math/vec4"


class Vec4Neg(Vec4UnaryOperator):
    def op_numpy(self, a: numpy.ndarray) -> numpy.ndarray:
        return -a

    CATEGORY = "math/vec4"


class Vec4Norm(Vec4ToScalarUnary):
    def op_numpy(self, a: numpy.ndarray) -> float:
        return numpy.linalg.norm(a).astype(float)

    CATEGORY = "math/vec4"


class Vec4Normalize(Vec4UnaryOperator):
    def op_numpy(self, a: numpy.ndarray) -> numpy.ndarray:
        return a / numpy.linalg.norm(a)

    CATEGORY = "math/vec4"


class Vec4Distance(Vec4ToScalarBinary):
    def op_numpy(self, a: numpy.ndarray, b: numpy.ndarray) -> float:
        return numpy.linalg.norm(a - b).astype(float)

    CATEGORY = "math/vec4"


class Vec4ScalarMul(Vec4ScalarOperation):
    def op_numpy(self, a: numpy.ndarray, b: float) -> numpy.ndarray:
        return a * b

    CATEGORY = "math/vec4"


NODE_CLASS_MAPPINGS = {
    "Vec4Add": Vec4Add,
    "Vec4Sub": Vec4Sub,
    "Vec4Dot": Vec4Dot,
    "Vec4Cross": Vec4Cross,
    "Vec4Eq": Vec4Eq,
    "Vec4Ne": Vec4Ne,
    "Vec4Neg": Vec4Neg,
    "Vec4Norm": Vec4Norm,
    "Vec4Normalize": Vec4Normalize,
    "Vec4Distance": Vec4Distance,
    "Vec4ScalarMul": Vec4ScalarMul,
}
