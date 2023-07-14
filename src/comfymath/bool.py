from abc import ABC, abstractmethod
from typing import Any, Mapping


class BoolPrimitive:
    def __init__(sefl):
        pass

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {"required": {"a": (["true", "false"],)}}

    RETURN_TYPES = ("BOOL",)
    FUNCTION = "op"
    CATEGORY = "math/bool"

    def op(self, a: str) -> bool:
        return True if a == "true" else False


class BoolUnaryOperator(ABC):
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {"required": {"a": ("BOOL", {"default": False})}}

    RETURN_TYPES = ("BOOL",)
    FUNCTION = "op"

    @abstractmethod
    def op(self, a: bool) -> bool:
        pass


class BoolBinaryOperator(ABC):
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls) -> Mapping[str, Any]:
        return {
            "required": {
                "a": ("BOOL", {"default": False}),
                "b": ("BOOL", {"default": False}),
            }
        }

    RETURN_TYPES = ("BOOL",)
    FUNCTION = "op"

    @abstractmethod
    def op(self, a: bool, b: bool) -> bool:
        pass


class BoolAnd(BoolBinaryOperator):
    def op(self, a: bool, b: bool) -> bool:
        return a and b

    CATEGORY = "math/bool"


class BoolOr(BoolBinaryOperator):
    def op(self, a: bool, b: bool) -> bool:
        return a or b

    CATEGORY = "math/bool"


class BoolNot(BoolUnaryOperator):
    def op(self, a: bool) -> bool:
        return not a

    CATEGORY = "math/bool"


class BoolXor(BoolBinaryOperator):
    def op(self, a: bool, b: bool) -> bool:
        return a ^ b

    CATEGORY = "math/bool"


class BoolXnor(BoolBinaryOperator):
    def op(self, a: bool, b: bool) -> bool:
        return not (a ^ b)

    CATEGORY = "math/bool"


class BoolNand(BoolBinaryOperator):
    def op(self, a: bool, b: bool) -> bool:
        return not (a and b)

    CATEGORY = "math/bool"


class BoolNor(BoolBinaryOperator):
    def op(self, a: bool, b: bool) -> bool:
        return not (a or b)

    CATEGORY = "math/bool"


class BoolEq(BoolBinaryOperator):
    def op(self, a: bool, b: bool) -> bool:
        return a == b

    CATEGORY = "math/bool/compare"


class BoolNe(BoolBinaryOperator):
    def op(self, a: bool, b: bool) -> bool:
        return a != b

    CATEGORY = "math/bool/compare"


NODE_CLASS_MAPPINGS = {
    "BoolPrimitive": BoolPrimitive,
    "BoolAnd": BoolAnd,
    "BoolOr": BoolOr,
    "BoolXor": BoolXor,
    "BoolNot": BoolNot,
    "BoolXnor": BoolXnor,
    "BoolNand": BoolNand,
    "BoolNor": BoolNor,
    "BoolEq": BoolEq,
    "BoolNe": BoolNe,
}
