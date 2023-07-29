from .src.comfymath.convert import NODE_CLASS_MAPPINGS as convert_NCM
from .src.comfymath.bool import NODE_CLASS_MAPPINGS as bool_NCM
from .src.comfymath.int import NODE_CLASS_MAPPINGS as int_NCM
from .src.comfymath.float import NODE_CLASS_MAPPINGS as float_NCM
from .src.comfymath.number import NODE_CLASS_MAPPINGS as number_NCM
from .src.comfymath.vec import NODE_CLASS_MAPPINGS as vec_NCM
from .src.comfymath.control import NODE_CLASS_MAPPINGS as control_NCM


NODE_CLASS_MAPPINGS = {
    **convert_NCM,
    **bool_NCM,
    **int_NCM,
    **float_NCM,
    **number_NCM,
    **vec_NCM,
    **control_NCM,
}


def remove_cm_prefix(node_mapping: str) -> str:
    if node_mapping.startswith("CM_"):
        return node_mapping[3:]
    return node_mapping


NODE_DISPLAY_NAME_MAPPINGS = {key: remove_cm_prefix(key) for key in NODE_CLASS_MAPPINGS}
