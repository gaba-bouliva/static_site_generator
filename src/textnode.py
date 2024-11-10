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

    def __eq__(self, textNode_2):
        if self.text != textNode_2.text:
            return False
        elif self.text_type != textNode_2.text_type:
            return False
        elif self.url != textNode_2.url:
            return False
        else:
            return True

    def __repr__(self):
        # print(f"TextNode: {self.text} {self.text_type} {self.url}")
        if self.text_type == TextType.BOLD.value:
            return f"Textnode({self.text.upper()}, {self.text_type.upper()}, {self.url.upper()})"
        elif self.text_type == TextType.ITALIC.value:
            return f"Textnode({self.text.lower()}, {self.text_type.lower()}, {self.url.lower()})"
        else:
            raise Exception("invalid text type")

        