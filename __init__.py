from .src.comfymath.convert import NODE_CLASS_MAPPINGS as convert_NCM
from .src.comfymath.int import NODE_CLASS_MAPPINGS as int_NCM
from .src.comfymath.float import NODE_CLASS_MAPPINGS as float_NCM
from .src.comfymath.vec2 import NODE_CLASS_MAPPINGS as vec2_NCM
from .src.comfymath.vec3 import NODE_CLASS_MAPPINGS as vec3_NCM
from .src.comfymath.vec4 import NODE_CLASS_MAPPINGS as vec4_NCM
from .src.comfymath.control import NODE_CLASS_MAPPINGS as control_NCM


NODE_CLASS_MAPPINGS = {
    **convert_NCM,
    **int_NCM,
    **float_NCM,
    **vec2_NCM,
    **vec3_NCM,
    **vec4_NCM,
    **control_NCM,
}

NODE_DISPLAY_NAME_MAPPINGS = {key: key for key in NODE_CLASS_MAPPINGS}
