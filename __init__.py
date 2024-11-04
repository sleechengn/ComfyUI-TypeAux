import os

class TextNode:

    @classmethod
    def INPUT_TYPES(s):
        return {"required": {"text": ("STRING", {"multiline": True, "dynamicPrompts": True})}}
    RETURN_TYPES = ("TEXT",)
    FUNCTION = "encode"

    CATEGORY = "ComfyUI-TypeAux"

    def encode(self,text):
        return (text, )

NODE_CLASS_MAPPINGS = {
        "PromptTextNode" : TextNode
}