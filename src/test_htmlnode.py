import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        empty_node = HTMLNode()
        node = HTMLNode("p","tag value")
        self.assertEqual("HTMLNode(p, tag value, children: None, None)", repr(node))
        self.assertEqual("HTMLNode(None, None, children: None, None)", repr(empty_node))
    
    def test_props(self):
        props = {"href": "https://www.google.com","target": "_blank"}
        node = HTMLNode("a", "link value", [], props)
        self.assertEqual(''' href="https://www.google.com" target="_blank"''', node.props_to_html())

if __name__ == "__main__":
    unittest.main()