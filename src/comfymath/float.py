import math

from abc import ABC, abstractmethod
from typing import Any, Mapping


class FloatUnaryOperator(ABC):
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {"required": {"a": ("FLOAT", {"default": 0.0})}}

    RETURN_TYPES = ("FLOAT",)
    FUNCTION = "op"

    @abstractmethod
    def op(self, a: float) -> tuple[float]:
        pass


class FloatBinaryOperator(ABC):
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {
            "required": {
                "a": ("FLOAT", {"default": 0.0}),
                "b": ("FLOAT", {"default": 0.0}),
            }
        }

    RETURN_TYPES = ("FLOAT",)
    FUNCTION = "op"

    @abstractmethod
    def op(self, a: float, b: float) -> tuple[float]:
        pass


class FloatUnaryQuery(ABC):
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {"required": {"a": ("FLOAT", {"default": 0.0})}}

    RETURN_TYPES = ("INT",)
    FUNCTION = "op"

    @abstractmethod
    def op(self, a: float) -> tuple[int]:
        pass


class FloatBinaryQuery(ABC):
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {
            "required": {
                "a": ("FLOAT", {"default": 0.0}),
                "b": ("FLOAT", {"default": 0.0}),
            }
        }

    RETURN_TYPES = ("INT",)
    FUNCTION = "op"

    @abstractmethod
    def op(self, a: float, b: float) -> tuple[int]:
        pass


class FloatAdd(FloatBinaryOperator):
    def op(self, a: float, b: float) -> tuple[float]:
        return (a + b,)

    CATEGORY = "math/float"


class FloatSub(FloatBinaryOperator):
    def op(self, a: float, b: float) -> tuple[float]:
        return (a - b,)

    CATEGORY = "math/float"


class FloatMul(FloatBinaryOperator):
    def op(self, a: float, b: float) -> tuple[float]:
        return (a * b,)

    CATEGORY = "math/float"


class FloatDiv(FloatBinaryOperator):
    def op(self, a: float, b: float) -> tuple[float]:
        return (a / b,)

    CATEGORY = "math/float"


class FloatLt(FloatBinaryQuery):
    def op(self, a: float, b: float) -> tuple[int]:
        return (int(a < b),)

    CATEGORY = "math/float/compare"


class FloatGt(FloatBinaryQuery):
    def op(self, a: float, b: float) -> tuple[int]:
        return (int(a > b),)

    CATEGORY = "math/float/compare"


class FloatLe(FloatBinaryQuery):
    def op(self, a: float, b: float) -> tuple[int]:
        return (int(a <= b),)

    CATEGORY = "math/float/compare"


class FloatGe(FloatBinaryQuery):
    def op(self, a: float, b: float) -> tuple[int]:
        return (int(a >= b),)

    CATEGORY = "math/float/compare"


class FloatEq(FloatBinaryQuery):
    def op(self, a: float, b: float) -> tuple[int]:
        return (int(a == b),)

    CATEGORY = "math/float/compare"


class FloatNe(FloatBinaryQuery):
    def op(self, a: float, b: float) -> tuple[int]:
        return (int(a != b),)

    CATEGORY = "math/float/compare"


class FloatNeg(FloatUnaryOperator):
    def op(self, a: float) -> tuple[float]:
        return (-a,)

    CATEGORY = "math/float"


class FloatInc(FloatUnaryOperator):
    def op(self, a: float) -> tuple[float]:
        return (a + 1,)

    CATEGORY = "math/float"


class FloatDec(FloatUnaryOperator):
    def op(self, a: float) -> tuple[float]:
        return (a - 1,)

    CATEGORY = "math/float"


class FloatAbs(FloatUnaryOperator):
    def op(self, a: float) -> tuple[float]:
        return (math.fabs(a),)

    CATEGORY = "math/float"


class FloatSqrt(FloatUnaryOperator):
    def op(self, a: float) -> tuple[float]:
        return (a**0.5,)

    CATEGORY = "math/float"


class FloatPow(FloatBinaryOperator):
    def op(self, a: float, b: float) -> tuple[float]:
        return (a**b,)

    CATEGORY = "math/float"


class FloatLog(FloatBinaryOperator):
    def op(self, a: float, b: float) -> tuple[float]:
        return (math.log(a, b),)

    CATEGORY = "math/float"


class FloatCeil(FloatUnaryOperator):
    def op(self, a: float) -> tuple[float]:
        return (math.ceil(a),)

    CATEGORY = "math/float"


class FloatFloor(FloatUnaryOperator):
    def op(self, a: float) -> tuple[float]:
        return (math.floor(a),)

    CATEGORY = "math/float"


class FloatRound(FloatUnaryOperator):
    def op(self, a: float) -> tuple[float]:
        return (round(a),)

    CATEGORY = "math/float"


class FloatTrunc(FloatUnaryOperator):
    def op(self, a: float) -> tuple[float]:
        return (math.trunc(a),)

    CATEGORY = "math/float"


class FloatSin(FloatUnaryOperator):
    def op(self, a: float) -> tuple[float]:
        return (math.sin(a),)

    CATEGORY = "math/float/trigonometry"


class FloatCos(FloatUnaryOperator):
    def op(self, a: float) -> tuple[float]:
        return (math.cos(a),)

    CATEGORY = "math/float/trigonometry"


class FloatTan(FloatUnaryOperator):
    def op(self, a: float) -> tuple[float]:
        return (math.tan(a),)

    CATEGORY = "math/float/trigonometry"


class FloatAsin(FloatUnaryOperator):
    def op(self, a: float) -> tuple[float]:
        return (math.asin(a),)

    CATEGORY = "math/float/trigonometry"


class FloatAcos(FloatUnaryOperator):
    def op(self, a: float) -> tuple[float]:
        return (math.acos(a),)

    CATEGORY = "math/float/trigonometry"


class FloatAtan(FloatUnaryOperator):
    def op(self, a: float) -> tuple[float]:
        return (math.atan(a),)

    CATEGORY = "math/float/trigonometry"


class FloatAtan2(FloatBinaryOperator):
    def op(self, a: float, b: float) -> tuple[float]:
        return (math.atan2(a, b),)

    CATEGORY = "math/float/trigonometry"


class FloatLn(FloatUnaryOperator):
    def op(self, a: float) -> tuple[float]:
        return (math.log(a),)

    CATEGORY = "math/float"


class FloatLog10(FloatUnaryOperator):
    def op(self, a: float) -> tuple[float]:
        return (math.log10(a),)

    CATEGORY = "math/float"


class FloatLog2(FloatUnaryOperator):
    def op(self, a: float) -> tuple[float]:
        return (math.log2(a),)

    CATEGORY = "math/float"


class FloatSinh(FloatUnaryOperator):
    def op(self, a: float) -> tuple[float]:
        return (math.sinh(a),)

    CATEGORY = "math/float/trigonometry"


class FloatCosh(FloatUnaryOperator):
    def op(self, a: float) -> tuple[float]:
        return (math.cosh(a),)

    CATEGORY = "math/float/trigonometry"


class FloatTanh(FloatUnaryOperator):
    def op(self, a: float) -> tuple[float]:
        return (math.tanh(a),)

    CATEGORY = "math/float/trigonometry"


class FloatAsinh(FloatUnaryOperator):
    def op(self, a: float) -> tuple[float]:
        return (math.asinh(a),)

    CATEGORY = "math/float/trigonometry"


class FloatAcosh(FloatUnaryOperator):
    def op(self, a: float) -> tuple[float]:
        return (math.acosh(a),)

    CATEGORY = "math/float/trigonometry"


class FloatAtanh(FloatUnaryOperator):
    def op(self, a: float) -> tuple[float]:
        return (math.atanh(a),)

    CATEGORY = "math/float/trigonometry"


class FloatExp(FloatUnaryOperator):
    def op(self, a: float) -> tuple[float]:
        return (math.exp(a),)

    CATEGORY = "math/float"


class FloatExpm1(FloatUnaryOperator):
    def op(self, a: float) -> tuple[float]:
        return (math.expm1(a),)

    CATEGORY = "math/float/functions"


class FloatErf(FloatUnaryOperator):
    def op(self, a: float) -> tuple[float]:
        return (math.erf(a),)

    CATEGORY = "math/float/functions"


class FloatErfc(FloatUnaryOperator):
    def op(self, a: float) -> tuple[float]:
        return (math.erfc(a),)

    CATEGORY = "math/float/functions"


class FloatGamma(FloatUnaryOperator):
    def op(self, a: float) -> tuple[float]:
        return (math.gamma(a),)

    CATEGORY = "math/float/functions"


class FloatRadians(FloatUnaryOperator):
    def op(self, a: float) -> tuple[float]:
        return (math.radians(a),)

    CATEGORY = "math/float/trigonometry"


class FloatDegrees(FloatUnaryOperator):
    def op(self, a: float) -> tuple[float]:
        return (math.degrees(a),)

    CATEGORY = "math/float/trigonometry"


NODE_CLASS_MAPPINGS = {
    "FloatAdd": FloatAdd,
    "FloatSub": FloatSub,
    "FloatMul": FloatMul,
    "FloatDiv": FloatDiv,
    "FloatLt": FloatLt,
    "FloatGt": FloatGt,
    "FloatLe": FloatLe,
    "FloatGe": FloatGe,
    "FloatEq": FloatEq,
    "FloatNe": FloatNe,
    "FloatNeg": FloatNeg,
    "FloatInc": FloatInc,
    "FloatDec": FloatDec,
    "FloatAbs": FloatAbs,
    "FloatAbs": FloatAbs,
    "FloatSqrt": FloatSqrt,
    "FloatPow": FloatPow,
    "FloatLog": FloatLog,
    "FloatCeil": FloatCeil,
    "FloatCeil": FloatCeil,
    "FloatFloor": FloatFloor,
    "FloatRound": FloatRound,
    "FloatTrunc": FloatTrunc,
    "FloatSin": FloatSin,
    "FloatCos": FloatCos,
    "FloatCos": FloatCos,
    "FloatTan": FloatTan,
    "FloatAsin": FloatAsin,
    "FloatAcos": FloatAcos,
    "FloatAtan": FloatAtan,
    "FloatAtan2": FloatAtan2,
    "FloatAtan2": FloatAtan2,
    "FloatLn": FloatLn,
    "FloatLog10": FloatLog10,
    "FloatLog2": FloatLog2,
    "FloatSinh": FloatSinh,
    "FloatCosh": FloatCosh,
    "FloatCosh": FloatCosh,
    "FloatTanh": FloatTanh,
    "FloatAsinh": FloatAsinh,
    "FloatAcosh": FloatAcosh,
    "FloatAtanh": FloatAtanh,
    "FloatExp": FloatExp,
    "FloatExpm1": FloatExpm1,
    "FloatExpm1": FloatExpm1,
    "FloatErf": FloatErf,
    "FloatErfc": FloatErfc,
    "FloatGamma": FloatGamma,
    "FloatRadians": FloatRadians,
    "FloatDegrees": FloatDegrees,
}
