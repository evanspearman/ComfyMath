import sys

if sys.version_info[1] < 10:
    from typing import Tuple, Union

    Number = Union[int, float]
    Vec2 = Tuple[float, float]
    Vec3 = Tuple[float, float, float]
    Vec4 = Tuple[float, float, float, float]
else:
    from typing import TypeAlias

    Number: TypeAlias = int | float
    Vec2: TypeAlias = tuple[float, float]
    Vec3: TypeAlias = tuple[float, float, float]
    Vec4: TypeAlias = tuple[float, float, float, float]
