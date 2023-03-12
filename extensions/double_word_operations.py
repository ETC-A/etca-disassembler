from decoder_lib import ExtensionRequirement, Extension
from .base_isa import SIZES

dw = Extension("double-word-operations", "d", (0, 14))

SIZES[2] = ('d', ExtensionRequirement.single(dw))
