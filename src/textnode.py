from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "Text"
    BOLD = "Bold"
    ITALIC = "Italic"
    CODE = "Code"
    LINK = "Link"
    IMAGE = "Image"

class TextNode:
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, other):
        return (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        )
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href":text_node.url})
        case TextType.IMAGE:
            return LeafNode("img", '', {"src":text_node.url, "alt":text_node.text})
        case _:
            raise ValueError(f"invalid text type: {text_node.text_type}")

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        # if not a text type node, just add it to new list and continue
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        node_text = node.text
        # find first delimiter
        start_index = node_text.find(delimiter)
        if start_index == -1:
            # delimiter not in text, keep old node as is
            new_nodes.append(node)
            continue
        # find closing delimiter
        end_index = node_text.find(delimiter, start_index + len(delimiter))
        if end_index == -1:
            # no closing tag, raise invalid Markdown exception
            raise Exception(f"Invalid Markdown syntax, no closing delimiter {delimiter} found")
        
        # extract the parts
        before_text = node_text[:start_index]
        delimiter_text = node_text[start_index + len(delimiter):end_index]
        after_text = node_text[end_index + len(delimiter):]
        # create new nodes and add to new list
        new_nodes.append(TextNode(before_text,TextType.TEXT))
        new_nodes.append(TextNode(delimiter_text, text_type))
        new_nodes.append(TextNode(after_text, TextType.TEXT))
    return new_nodes



