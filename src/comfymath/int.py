import math

from dataclasses import dataclass
from typing import Callable, TypeAlias


@dataclass
class IntUnaryOperation:
    name: str
    function: Callable[[int], int]


@dataclass
class IntUnaryCondition:
    name: str
    function: Callable[[int], bool]


@dataclass
class IntBinaryOperation:
    name: str
    function: Callable[[int, int], int]


@dataclass
class IntBinaryCondition:
    name: str
    function: Callable[[int, int], bool]


INT_UNARY_OPERATIONS = [
    IntUnaryOperation("Abs", lambda a: abs(a)),
    IntUnaryOperation("Neg", lambda a: -a),
    IntUnaryOperation("Inc", lambda a: a + 1),
    IntUnaryOperation("Dec", lambda a: a - 1),
    IntUnaryOperation("Sqr", lambda a: a * a),
    IntUnaryOperation("Cube", lambda a: a * a * a),
    IntUnaryOperation("Not", lambda a: ~a),
    IntUnaryOperation("Factorial", lambda a: math.factorial(a)),
]

INT_UNARY_CONDITIONS = [
    IntUnaryCondition("IsZero", lambda a: a == 0),
    IntUnaryCondition("IsNonZero", lambda a: a != 0),
    IntUnaryCondition("IsPositive", lambda a: a > 0),
    IntUnaryCondition("IsNegative", lambda a: a < 0),
    IntUnaryCondition("IsEven", lambda a: a % 2 == 0),
    IntUnaryCondition("IsOdd", lambda a: a % 2 == 1),
]

INT_BINARY_OPERATIONS = [
    IntBinaryOperation("Add", lambda a, b: a + b),
    IntBinaryOperation("Sub", lambda a, b: a - b),
    IntBinaryOperation("Mul", lambda a, b: a * b),
    IntBinaryOperation("Div", lambda a, b: a // b),
    IntBinaryOperation("Mod", lambda a, b: a % b),
    IntBinaryOperation("Pow", lambda a, b: a**b),
    IntBinaryOperation("And", lambda a, b: a & b),
    IntBinaryOperation("Nand", lambda a, b: ~a & b),
    IntBinaryOperation("Or", lambda a, b: a | b),
    IntBinaryOperation("Nor", lambda a, b: ~a & b),
    IntBinaryOperation("Xor", lambda a, b: a ^ b),
    IntBinaryOperation("Xnor", lambda a, b: ~a ^ b),
    IntBinaryOperation("Shl", lambda a, b: a << b),
    IntBinaryOperation("Shr", lambda a, b: a >> b),
    IntBinaryOperation("Max", lambda a, b: max(a, b)),
    IntBinaryOperation("Min", lambda a, b: min(a, b)),
]

INT_BINARY_CONDITIONS = [
    IntBinaryCondition("Eq", lambda a, b: a == b),
    IntBinaryCondition("Neq", lambda a, b: a != b),
    IntBinaryCondition("Gt", lambda a, b: a > b),
    IntBinaryCondition("Lt", lambda a, b: a < b),
    IntBinaryCondition("Geq", lambda a, b: a >= b),
    IntBinaryCondition("Leq", lambda a, b: a <= b),
]


def _get_int_unary_op_node_class(op: IntUnaryOperation) -> type:
    name = f"Int{op.name}"
    class_dict = {
        "INPUT_TYPES": lambda: {"required": {"a": ("INT", {"default": 0})}},
        "RETURN_TYPES": ("INT",),
        "FUNCTION": "op",
        "CATEGORY": "math/int",
        "op": lambda a: op.function(a),
    }
    return type(name, (), class_dict)

def _get_int_unary_cond_node_class(op: IntUnaryCondition) -> type:
    name = f"Int{op.name}"
    class_dict = {
        "INPUT_TYPES": lambda: {"required": {"a": ("INT", {"default": 0})}},
        "RETURN_TYPES": ("INT",),
        "FUNCTION": "op",
        "CATEGORY": "math/int",
        "op": lambda a: int(op.function(a)),
    }
    return type(name, (), class_dict)


def _get_int_binary_op_node_class(op: IntBinaryOperation) -> type:
    name = f"Int{op.name}"
    class_dict = {
        "INPUT_TYPES": lambda: {
            "required": {"a": ("INT", {"default": 0}), "b": ("INT", {"default": 0})}
        },
        "RETURN_TYPES": ("INT",),
        "FUNCTION": "op",
        "CATEGORY": "math/int",
        "op": lambda a, b: op.function(a, b),
    }
    return type(name, (), class_dict)

def _get_int_binary_cond_node_class(op: IntBinaryCondition) -> type:
    name = f"Int{op.name}"
    class_dict = {
        "INPUT_TYPES": lambda: {
            "required": {"a": ("INT", {"default": 0}), "b": ("INT", {"default": 0})}
        },
        "RETURN_TYPES": ("INT",),
        "FUNCTION": "op",
        "CATEGORY": "math/int",
        "op": lambda a, b: int(op.function(a, b)),
    }
    return type(name, (), class_dict)


FLOAT_UNARY_OPERATION_CLASS_MAPPINGS = {
    f"Int{op.name}": _get_int_unary_op_node_class(op) for op in INT_UNARY_OPERATIONS
}

FLOAT_UNARY_CONDITION_CLASS_MAPPINGS = {
    f"Int{op.name}": _get_int_unary_cond_node_class(op) for op in INT_UNARY_CONDITIONS
}

FLOAT_BINARY_OPERATION_CLASS_MAPPINGS = {
    f"Int{op.name}": _get_int_binary_op_node_class(op) for op in INT_BINARY_OPERATIONS
}

FLOAT_BINARY_CONDITION_CLASS_MAPPINGS = {
    f"Int{op.name}": _get_int_binary_cond_node_class(op) for op in INT_BINARY_CONDITIONS
}

NODE_CLASS_MAPPINGS = {
    **FLOAT_UNARY_OPERATION_CLASS_MAPPINGS,
    **FLOAT_UNARY_CONDITION_CLASS_MAPPINGS,
    **FLOAT_BINARY_OPERATION_CLASS_MAPPINGS,
    **FLOAT_BINARY_CONDITION_CLASS_MAPPINGS,
}
