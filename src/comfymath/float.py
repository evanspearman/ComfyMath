import math

from dataclasses import dataclass
from typing import Callable


@dataclass
class FloatUnaryOperation:
    name: str
    function: Callable[[float], float]


@dataclass
class FloatUnaryCondition:
    name: str
    function: Callable[[float], bool]


@dataclass
class FloatBinaryOperation:
    name: str
    function: Callable[[float, float], float]


@dataclass
class FloatBinaryCondition:
    name: str
    function: Callable[[float, float], bool]


FLOAT_UNARY_OPERATIONS = [
    FloatUnaryOperation("Neg", lambda a: -a),
    FloatUnaryOperation("Inc", lambda a: a + 1),
    FloatUnaryOperation("Dec", lambda a: a - 1),
    FloatUnaryOperation("Abs", lambda a: abs(a)),
    FloatUnaryOperation("Sqr", lambda a: a * a),
    FloatUnaryOperation("Cube", lambda a: a * a * a),
    FloatUnaryOperation("Sqrt", lambda a: math.sqrt(a)),
    FloatUnaryOperation("Exp", lambda a: math.exp(a)),
    FloatUnaryOperation("Ln", lambda a: math.log(a)),
    FloatUnaryOperation("Log10", lambda a: math.log10(a)),
    FloatUnaryOperation("Log2", lambda a: math.log2(a)),
    FloatUnaryOperation("Sin", lambda a: math.sin(a)),
    FloatUnaryOperation("Cos", lambda a: math.cos(a)),
    FloatUnaryOperation("Tan", lambda a: math.tan(a)),
    FloatUnaryOperation("Asin", lambda a: math.asin(a)),
    FloatUnaryOperation("Acos", lambda a: math.acos(a)),
    FloatUnaryOperation("Atan", lambda a: math.atan(a)),
    FloatUnaryOperation("Sinh", lambda a: math.sinh(a)),
    FloatUnaryOperation("Cosh", lambda a: math.cosh(a)),
    FloatUnaryOperation("Tanh", lambda a: math.tanh(a)),
    FloatUnaryOperation("Asinh", lambda a: math.asinh(a)),
    FloatUnaryOperation("Acosh", lambda a: math.acosh(a)),
    FloatUnaryOperation("Atanh", lambda a: math.atanh(a)),
    FloatUnaryOperation("Round", lambda a: round(a)),
    FloatUnaryOperation("Floor", lambda a: math.floor(a)),
    FloatUnaryOperation("Ceil", lambda a: math.ceil(a)),
    FloatUnaryOperation("Trunc", lambda a: math.trunc(a)),
    FloatUnaryOperation("Erf", lambda a: math.erf(a)),
    FloatUnaryOperation("Erfc", lambda a: math.erfc(a)),
    FloatUnaryOperation("Gamma", lambda a: math.gamma(a)),
    FloatUnaryOperation("Radians", lambda a: math.radians(a)),
    FloatUnaryOperation("Degrees", lambda a: math.degrees(a)),
]

FLOAT_UNARY_CONDITIONS = [
    FloatUnaryCondition("IsZero", lambda a: a == 0.0),
    FloatUnaryCondition("IsPositive", lambda a: a > 0.0),
    FloatUnaryCondition("IsNegative", lambda a: a < 0.0),
    FloatUnaryCondition("IsNonZero", lambda a: a != 0.0),
    FloatUnaryCondition("IsPositiveInfinity", lambda a: math.isinf(a) and a > 0.0),
    FloatUnaryCondition("IsNegativeInfinity", lambda a: math.isinf(a) and a < 0.0),
    FloatUnaryCondition("IsNaN", lambda a: math.isnan(a)),
    FloatUnaryCondition("IsFinite", lambda a: math.isfinite(a)),
    FloatUnaryCondition("IsInfinite", lambda a: math.isinf(a)),
    FloatUnaryCondition("IsEven", lambda a: a % 2 == 0.0),
    FloatUnaryCondition("IsOdd", lambda a: a % 2 != 0.0),
]

FLOAT_BINARY_OPERATIONS = [
    FloatBinaryOperation("Add", lambda a, b: a + b),
    FloatBinaryOperation("Sub", lambda a, b: a - b),
    FloatBinaryOperation("Mul", lambda a, b: a * b),
    FloatBinaryOperation("Div", lambda a, b: a / b),
    FloatBinaryOperation("Mod", lambda a, b: a % b),
    FloatBinaryOperation("Pow", lambda a, b: a**b),
    FloatBinaryOperation("FloorDiv", lambda a, b: a // b),
    FloatBinaryOperation("Max", lambda a, b: max(a, b)),
    FloatBinaryOperation("Min", lambda a, b: min(a, b)),
    FloatBinaryOperation("Log", lambda a, b: math.log(a, b)),
    FloatBinaryOperation("Atan2", lambda a, b: math.atan2(a, b)),
]

FLOAT_BINARY_CONDITIONS = [
    FloatBinaryCondition("Eq", lambda a, b: a == b),
    FloatBinaryCondition("Neq", lambda a, b: a != b),
    FloatBinaryCondition("Gt", lambda a, b: a > b),
    FloatBinaryCondition("Gte", lambda a, b: a >= b),
    FloatBinaryCondition("Lt", lambda a, b: a < b),
    FloatBinaryCondition("Lte", lambda a, b: a <= b),
]


def _get_float_unary_op_node_class(op: FloatUnaryOperation) -> type:
    name = f"Float{op.name}"
    class_dict = {
        "INPUT_TYPES": lambda: {"required": {"a": ("FLOAT", {"default": 0.0})}},
        "RETURN_TYPES": ("FLOAT",),
        "FUNCTION": "op",
        "CATEGORY": "math/float",
        "op": op.function,
    }
    return type(name, (), class_dict)


def _get_float_unary_cond_node_class(op: FloatUnaryCondition) -> type:
    name = f"Float{op.name}"
    class_dict = {
        "INPUT_TYPES": lambda: {"required": {"a": ("FLOAT", {"default": 0.0})}},
        "RETURN_TYPES": ("INT",),
        "FUNCTION": "op",
        "CATEGORY": "math/float",
        "op": lambda a: int(op.function(a)),
    }
    return type(name, (), class_dict)


def _get_float_binary_op_node_class(op: FloatBinaryOperation) -> type:
    name = f"Float{op.name}"
    class_dict = {
        "INPUT_TYPES": lambda: {
            "required": {
                "a": ("FLOAT", {"default": 0.0}),
                "b": ("FLOAT", {"default": 0.0}),
            }
        },
        "RETURN_TYPES": ("FLOAT",),
        "FUNCTION": "op",
        "CATEGORY": "math/float",
        "op": op.function,
    }
    return type(name, (), class_dict)


def _get_float_binary_cond_node_class(op: FloatBinaryCondition) -> type:
    name = f"Float{op.name}"
    class_dict = {
        "INPUT_TYPES": lambda: {
            "required": {
                "a": ("FLOAT", {"default": 0.0}),
                "b": ("FLOAT", {"default": 0.0}),
            }
        },
        "RETURN_TYPES": ("INT",),
        "FUNCTION": "op",
        "CATEGORY": "math/float",
        "op": lambda a, b: int(op.function(a, b)),
    }
    return type(name, (), class_dict)


FLOAT_UNARY_OPERATION_CLASS_MAPPINGS = {
    f"Float{op.name}": _get_float_unary_op_node_class(op)
    for op in FLOAT_UNARY_OPERATIONS
}

FLOAT_UNARY_CONDITION_CLASS_MAPPINGS = {
    f"Float{op.name}": _get_float_unary_cond_node_class(op)
    for op in FLOAT_UNARY_CONDITIONS
}


FLOAT_BINARY_OPERATION_CLASS_MAPPINGS = {
    f"Float{op.name}": _get_float_binary_op_node_class(op)
    for op in FLOAT_BINARY_OPERATIONS
}

FLOAT_BINARY_CONDITION_CLASS_MAPPINGS = {
    f"Float{op.name}": _get_float_binary_cond_node_class(op)
    for op in FLOAT_BINARY_CONDITIONS
}

NODE_CLASS_MAPPINGS = {
    **FLOAT_UNARY_OPERATION_CLASS_MAPPINGS,
    **FLOAT_UNARY_CONDITION_CLASS_MAPPINGS,
    **FLOAT_BINARY_OPERATION_CLASS_MAPPINGS,
    **FLOAT_BINARY_CONDITION_CLASS_MAPPINGS,
}
