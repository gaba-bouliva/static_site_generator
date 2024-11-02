from enum import Enum

class NodeType(Enum):
    HTML = "html"
    LEAF = "leaf"
    TEXT = "text"

class TextType(Enum):
    BOLD = "bold"
    ITALIC = "italic"

class TextNode:
    def __init__(self, text, text_type, url=None):
        if text_type == TextType.BOLD:
            self.text_type = text_type.value
        elif text_type == TextType.ITALIC:
            self.text_type = text_type.value
        else:
            raise Exception("invalid text type")
            
        self.text = text
        self.url = url

    def __eq__(self, textNode):
        for prop in textNode:
            if textNode[prop] != self[prop]:
                return False
        return True

    def __repr__(self):
        if self.text_type == 'bold':
            return f"Textnode({self.text.upper()}, {self.text_type.upper()}, {self.url.upper()}"
        elif self.text_type == TextType.ITALIC:
            return f"Textnode({self.text.lower()}, {self.text_type.lower()}, {self.url.upper()}"
        else:
            raise Exception("invalid text type")

        