from enum import Enum

class TextType(Enum):
    NORMAL_TEXT = "Normal"
    BOLD_TEXT = "Bold"
    ITALIC_TEXT = "Italic"
    CODE_TEXT = "Code"
    LINK = "Link"
    IMAGE = "Image"

class TextNode:
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other):
        return self.text == other.text and self.text_type.value == other.text_type.value and self.url == other.url
    
    def __repr__(self):
        return "TextNode({}, {}, {})".format(self.text, self.text_type, self.url)