from .nodes.PromptTextNode import PromptTextNode
from .nodes.StringReplace import StringReplace

NODE_CLASS_MAPPINGS = {
        "PromptTextNodeFunction" : PromptTextNode,
        "StringReplaceFunction" : StringReplace
}