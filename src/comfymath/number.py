from dataclasses import dataclass
from typing import Callable, TypeAlias, Sequence

from .int import (
    INT_UNARY_OPERATIONS,
    INT_UNARY_CONDITIONS,
    INT_BINARY_OPERATIONS,
    INT_BINARY_CONDITIONS,
)
from .float import (
    FLOAT_UNARY_OPERATIONS,
    FLOAT_UNARY_CONDITIONS,
    FLOAT_BINARY_OPERATIONS,
    FLOAT_BINARY_CONDITIONS,
    FloatUnaryOperation,
    FloatUnaryCondition,
    FloatBinaryOperation,
    FloatBinaryCondition,
)

number: TypeAlias = int | float


@dataclass
class NumberUnaryOperation:
    name: str
    function: Callable[[number], number]


@dataclass
class NumberUnaryCondition:
    name: str
    function: Callable[[number], bool]


@dataclass
class NumberBinaryOperation:
    name: str
    function: Callable[[number, number], number]


@dataclass
class NumberBinaryCondition:
    name: str
    function: Callable[[number, number], bool]


def _float_unary_operation_to_num_unary_operation(
    op: FloatUnaryOperation,
) -> NumberUnaryOperation:
    return NumberUnaryOperation(op.name, op.function)


def _float_unary_condition_to_num_unary_condition(
    op: FloatUnaryCondition,
) -> NumberUnaryCondition:
    return NumberUnaryCondition(op.name, op.function)


def _float_binary_operation_to_num_binary_operation(
    op: FloatBinaryOperation,
) -> NumberBinaryOperation:
    return NumberBinaryOperation(op.name, op.function)


def _float_binary_condition_to_num_binary_condition(
    op: FloatBinaryCondition,
) -> NumberBinaryCondition:
    return NumberBinaryCondition(op.name, op.function)


def _combine_unary_operations() -> Sequence[NumberUnaryOperation]:
    float_unary_op_names = {op.name for op in FLOAT_UNARY_OPERATIONS}
    int_unary_op_names = {op.name for op in INT_UNARY_OPERATIONS}
    num_unary_op_names = float_unary_op_names & int_unary_op_names
    return [
        _float_unary_operation_to_num_unary_operation(op)
        for op in FLOAT_UNARY_OPERATIONS
        if op.name in num_unary_op_names
    ]


def _combine_unary_conditions() -> Sequence[NumberUnaryCondition]:
    float_unary_cond_names = {op.name for op in FLOAT_UNARY_CONDITIONS}
    int_unary_cond_names = {op.name for op in INT_UNARY_CONDITIONS}
    num_unary_cond_names = float_unary_cond_names & int_unary_cond_names
    return [
        _float_unary_condition_to_num_unary_condition(op)
        for op in FLOAT_UNARY_CONDITIONS
        if op.name in num_unary_cond_names
    ]


def _combine_binary_operations() -> Sequence[NumberBinaryOperation]:
    float_binary_op_names = {op.name for op in FLOAT_BINARY_OPERATIONS}
    int_binary_op_names = {op.name for op in INT_BINARY_OPERATIONS}
    num_binary_op_names = float_binary_op_names & int_binary_op_names
    return [
        _float_binary_operation_to_num_binary_operation(op)
        for op in FLOAT_BINARY_OPERATIONS
        if op.name in num_binary_op_names
    ]


def _combine_binary_conditions() -> Sequence[NumberBinaryCondition]:
    float_binary_cond_names = {op.name for op in FLOAT_BINARY_CONDITIONS}
    int_binary_cond_names = {op.name for op in INT_BINARY_CONDITIONS}
    num_binary_cond_names = float_binary_cond_names & int_binary_cond_names
    return [
        _float_binary_condition_to_num_binary_condition(op)
        for op in FLOAT_BINARY_CONDITIONS
        if op.name in num_binary_cond_names
    ]


def _get_number_unary_op_node_class(op: NumberUnaryOperation) -> type:
    name = f"Number{op.name}"
    class_dict = {
        "INPUT_TYPES": lambda: {"required": {"a": ("NUMBER", {"default": 0.0})}},
        "RETURN_TYPES": ("NUMBER",),
        "FUNCTION": "op",
        "CATEGORY": "math/number",
        "op": op.function,
    }
    return type(name, (), class_dict)


def _get_number_unary_cond_node_class(op: NumberUnaryCondition) -> type:
    name = f"Number{op.name}"
    class_dict = {
        "INPUT_TYPES": lambda: {"required": {"a": ("NUMBER", {"default": 0.0})}},
        "RETURN_TYPES": ("INT",),
        "FUNCTION": "op",
        "CATEGORY": "math/number",
        "op": lambda a: int(op.function(a)),
    }
    return type(name, (), class_dict)


def _get_number_binary_op_node_class(op: NumberBinaryOperation) -> type:
    name = f"Number{op.name}"
    class_dict = {
        "INPUT_TYPES": lambda: {
            "required": {
                "a": ("NUMBER", {"default": 0.0}),
                "b": ("NUMBER", {"default": 0.0}),
            }
        },
        "RETURN_TYPES": ("NUMBER",),
        "FUNCTION": "op",
        "CATEGORY": "math/number",
        "op": op.function,
    }
    return type(name, (), class_dict)


def _get_number_binary_cond_node_class(op: NumberBinaryCondition) -> type:
    name = f"Number{op.name}"
    class_dict = {
        "INPUT_TYPES": lambda: {
            "required": {
                "a": ("NUMBER", {"default": 0.0}),
                "b": ("NUMBER", {"default": 0.0}),
            }
        },
        "RETURN_TYPES": ("NUMBER",),
        "FUNCTION": "op",
        "CATEGORY": "math/number",
        "op": lambda a, b: int(op.function(a, b)),
    }
    return type(name, (), class_dict)


NUMBER_UNARY_OPERATIONS = _combine_unary_operations()
NUMBER_UNARY_CONDITIONS = _combine_unary_conditions()
NUMBER_BINARY_OPERATIONS = _combine_binary_operations()
NUMBER_BINARY_CONDITIONS = _combine_binary_conditions()

NUMBER_UNARY_OPERATION_CLASS_MAPPINGS = {
    f"Number{op.name}": _get_number_unary_op_node_class(op)
    for op in NUMBER_UNARY_OPERATIONS
}

NUMBER_UNARY_CONDITION_CLASS_MAPPINGS = {
    f"Number{op.name}": _get_number_unary_cond_node_class(op)
    for op in NUMBER_UNARY_CONDITIONS
}


NUMBER_BINARY_OPERATION_CLASS_MAPPINGS = {
    f"Number{op.name}": _get_number_binary_op_node_class(op)
    for op in NUMBER_BINARY_OPERATIONS
}

NUMBER_BINARY_CONDITION_CLASS_MAPPINGS = {
    f"Number{op.name}": _get_number_binary_cond_node_class(op)
    for op in NUMBER_BINARY_CONDITIONS
}

NODE_CLASS_MAPPINGS = {
    **NUMBER_UNARY_OPERATION_CLASS_MAPPINGS,
    **NUMBER_UNARY_CONDITION_CLASS_MAPPINGS,
    **NUMBER_BINARY_OPERATION_CLASS_MAPPINGS,
    **NUMBER_BINARY_CONDITION_CLASS_MAPPINGS,
}
