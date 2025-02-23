import unittest
from textnode import TextType, TextNode

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
    
if __name__ == "__main__":
    unittest.main()