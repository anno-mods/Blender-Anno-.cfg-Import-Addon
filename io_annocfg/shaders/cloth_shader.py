import bpy
from .shader_base import AnnoBasicShader
from .shader_components import *
from .shader_node_templates import ShaderTemplate

from ..utils import to_data_path
import os
from pathlib import Path
from ..prefs import IO_AnnocfgPreferences

class ClothShader(AnnoBasicShader):

    def __init__(self):
        super().__init__()

        self.shader_id = "AnnoClothShader"

        self.compose(ClothShaderComponent())
        self.compose(AtlasComponent())
        self.compose(RimEffectComponent())
        self.compose(RipplesComponent())
        self.compose(MiniTerrainAdapion())
        self.add_link(FlagLink("Disable Revive Distance", "DisableReviveDistance"))

        # override default vertexformat
        self.material_properties["VertexFormat"] = "P3f_N3b,T2f"
        self.material_properties["ShaderID"] = "0"

    def create_anno_shader(self):
        anno_shader = self.setup_empty_shader()
                
        shader_template = ShaderTemplate(anno_shader)
        diff = shader_template.add_diffuse("cDiffuse", "cDiffuseMultiplier")
        shader_template.add_dye(diff)
        shader_template.add_normal("cNormal")
        shader_template.add_gloss("Glossiness")