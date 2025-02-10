import os
import re

class StringReplace:

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING",{"defaultInput": True, "default": "{}", "multiline": True}),
                "match": ("STRING",{"defaultInput": True, "default": "{}", "multiline": True}),
                "value": ("STRING",{"defaultInput": True, "default": "", "dynamicPrompts": True,"multiline": True}),
                "match_type": (["text", "regex"], {"default": "regex"}),
            }
        }

    RETURN_TYPES = ("STRING", )
    FUNCTION = "encode"

    CATEGORY = "ComfyUI-TypeAux"

    def encode(self, text, match, value, match_type):
        if match_type == "regex":
            pattern = re.compile(match,re.DOTALL)
            return (re.sub(pattern, value, text),)
        if match_type == "text":
            return text.replace(match,value)