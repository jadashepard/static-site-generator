import unittest
from textnode import TextType, TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("this is a test node", TextType.BOLD)
        node2 = TextNode("this is a test node", TextType.BOLD)
        node3 = TextNode("this is a test node", TextType.ITALIC)
        node4 = TextNode("this is a test node", TextType.BOLD, None)
        node5 = TextNode("I am a test node", TextType.BOLD)
        self.assertEqual(node, node2)
        self.assertEqual(node, node4)
        self.assertNotEqual(node, node3)
        self.assertNotEqual(node2, node5)

if __name__ == "__main__":
    unittest.main()