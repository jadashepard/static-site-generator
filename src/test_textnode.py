import unittest
from textnode import TextType, TextNode, text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("this is a test node", TextType.BOLD)
        node2 = TextNode("this is a test node", TextType.BOLD)
        node3 = TextNode("this is a test node", TextType.BOLD, None)
        node4 = TextNode("I am a test node", TextType.BOLD, "https://localhost:8888")
        node5 = TextNode("I am a test node", TextType.BOLD, "https://localhost:8888")
        self.assertEqual(node, node2)
        self.assertEqual(node, node3)
        self.assertEqual(node4, node5)
    
    def test_eq_text_false(self):
        node = TextNode("this is a test node", TextType.BOLD)
        node2 = TextNode("I am a test node", TextType.BOLD)
        self.assertNotEqual(node, node2)
    
    def test_eq_type_false(self):
        node = TextNode("this is a test node", TextType.BOLD)
        node2 = TextNode("this is a test node", TextType.ITALIC)
        self.assertNotEqual(node, node2)
    
    def test_eq_url_false(self):
        node = TextNode("this is a test node", TextType.BOLD, "https://localhost:8888")
        node2 = TextNode("this is a test node", TextType.BOLD)
        self.assertNotEqual(node, node2)
    
    def test_repr(self):
        node = TextNode("this is a test node", TextType.BOLD, "https://localhost:8888")
        self.assertEqual(
            "TextNode(this is a test node, Bold, https://localhost:8888)", repr(node)
        )

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")
    
if __name__ == "__main__":
    unittest.main()