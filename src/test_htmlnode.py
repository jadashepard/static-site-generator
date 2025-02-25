import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        empty_node = HTMLNode()
        node = HTMLNode("p","tag value")
        self.assertEqual("HTMLNode(p, tag value, children: None, None)", node.__repr__())
        self.assertEqual("HTMLNode(None, None, children: None, None)", empty_node.__repr__())
    
    def test_props(self):
        props = {"href": "https://www.google.com","target": "_blank"}
        node = HTMLNode("a", "link value", [], props)
        self.assertEqual(''' href="https://www.google.com" target="_blank"''', node.props_to_html())
    
    def test_leaf_to_html(self):
        leaf_node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        leaf_node2 = LeafNode(None, "raw text value")
        self.assertEqual(
            '''<a href="https://www.google.com">Click me!</a>''', leaf_node.to_html()
        )
        self.assertEqual(
            "raw text value", leaf_node2.to_html()
        )

if __name__ == "__main__":
    unittest.main()