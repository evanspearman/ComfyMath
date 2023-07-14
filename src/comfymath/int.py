import math

from abc import ABC, abstractmethod
from typing import Any, Mapping


class IntUnaryOperator(ABC):
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {"required": {"a": ("INT", {"default": 0})}}

    RETURN_TYPES = ("INT",)
    FUNCTION = "op"

    @abstractmethod
    def op(self, a: int) -> int:
        pass


class IntBinaryOperator(ABC):
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {
            "required": {"a": ("INT", {"default": 0}), "b": ("INT", {"default": 0})}
        }

    RETURN_TYPES = ("INT",)
    FUNCTION = "op"

    @abstractmethod
    def op(self, a: int, b: int) -> int:
        pass


class IntUnaryQuery(ABC):
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {"required": {"a": ("INT", {"default": 0})}}

    RETURN_TYPES = ("BOOL",)
    FUNCTION = "op"

    @abstractmethod
    def op(self, a: int) -> bool:
        pass


class IntBinaryQuery(ABC):
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {
            "required": {
                "a": ("INT", {"default": 0}),
                "b": ("INT", {"default": 0}),
            }
        }

    RETURN_TYPES = ("BOOL",)
    FUNCTION = "op"

    @abstractmethod
    def op(self, a: int, b: int) -> bool:
        pass


class IntAdd(IntBinaryOperator):
    def op(self, a: int, b: int) -> int:
        return a + b

    CATEGORY = "math/int"


class IntSub(IntBinaryOperator):
    def op(self, a: int, b: int) -> int:
        return a - b

    CATEGORY = "math/int"


class IntMul(IntBinaryOperator):
    def op(self, a: int, b: int) -> int:
        return a * b

    CATEGORY = "math/int"


class IntDiv(IntBinaryOperator):
    def op(self, a: int, b: int) -> int:
        return a // b

    CATEGORY = "math/int"


class IntMod(IntBinaryOperator):
    def op(self, a: int, b: int) -> int:
        return a % b

    CATEGORY = "math/int"


class IntPow(IntBinaryOperator):
    def op(self, a: int, b: int) -> int:
        return a**b

    CATEGORY = "math/int"


class IntLt(IntBinaryQuery):
    def op(self, a: int, b: int) -> bool:
        return a < b

    CATEGORY = "math/int/compare"


class IntGt(IntBinaryQuery):
    def op(self, a: int, b: int) -> bool:
        return a > b

    CATEGORY = "math/int/compare"


class IntLe(IntBinaryQuery):
    def op(self, a: int, b: int) -> bool:
        return a <= b

    CATEGORY = "math/int/compare"


class IntGe(IntBinaryQuery):
    def op(self, a: int, b: int) -> bool:
        return a >= b

    CATEGORY = "math/int/compare"


class IntEq(IntBinaryQuery):
    def op(self, a: int, b: int) -> bool:
        return a == b

    CATEGORY = "math/int/compare"


class IntNe(IntBinaryQuery):
    def op(self, a: int, b: int) -> bool:
        return a != b

    CATEGORY = "math/int/compare"


class IntAnd(IntBinaryOperator):
    def op(self, a: int, b: int) -> int:
        return a & b

    CATEGORY = "math/int/bitwise"


class IntOr(IntBinaryOperator):
    def op(self, a: int, b: int) -> int:
        return a | b

    CATEGORY = "math/int/bitwise"


class IntXor(IntBinaryOperator):
    def op(self, a: int, b: int) -> int:
        return a ^ b

    CATEGORY = "math/int/bitwise"


class IntNot(IntUnaryOperator):
    def op(self, a: int) -> int:
        return ~a

    CATEGORY = "math/int/bitwise"


class IntNeg(IntUnaryOperator):
    def op(self, a: int) -> int:
        return -a

    CATEGORY = "math/int"


class IntInc(IntUnaryOperator):
    def op(self, a: int) -> int:
        return a + 1

    CATEGORY = "math/int"


class IntDec(IntUnaryOperator):
    def op(self, a: int) -> int:
        return a - 1

    CATEGORY = "math/int"


class IntAbs(IntUnaryOperator):
    def op(self, a: int) -> int:
        return abs(a)

    CATEGORY = "math/int"


class IntFactorial(IntUnaryOperator):
    def op(self, a: int) -> int:
        return math.factorial(a)

    CATEGORY = "math/int"


NODE_CLASS_MAPPINGS = {
    "IntAdd": IntAdd,
    "IntSub": IntSub,
    "IntMul": IntMul,
    "IntDiv": IntDiv,
    "IntLt": IntLt,
    "IntGt": IntGt,
    "IntLe": IntLe,
    "IntGe": IntGe,
    "IntEq": IntEq,
    "IntNe": IntNe,
    "IntAnd": IntAnd,
    "IntOr": IntOr,
    "IntXor": IntXor,
    "IntNot": IntNot,
    "IntNeg": IntNeg,
    "IntInc": IntInc,
    "IntInc": IntInc,
    "IntDec": IntDec,
    "IntAbs": IntAbs,
    "IntFactorial": IntFactorial,
}
