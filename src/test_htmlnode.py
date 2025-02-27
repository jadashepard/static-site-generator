import unittest
from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode

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
    
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")
    
    def test_to_html_with_children2(self):
        child_node1 = LeafNode("span", "child1")
        child_node2 = LeafNode("span", "child2")
        child_node3 = LeafNode("span", "child3")
        parent_node = ParentNode("div", [child_node1, child_node2, child_node3])
        self.assertEqual(parent_node.to_html(), "<div><span>child1</span><span>child2</span><span>child3</span></div>")
    
    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_to_html_with_grandchildren2(self):
        grandchild_node1 = LeafNode("b", "grandchild1")
        grandchild_node2 = LeafNode("b", "grandchild2")
        child_node1 = ParentNode("span", [grandchild_node1, grandchild_node2])
        child_node2 = ParentNode("span", [grandchild_node1, grandchild_node2])
        parent_node = ParentNode("div", [child_node1, child_node2])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild1</b><b>grandchild2</b></span><span><b>grandchild1</b><b>grandchild2</b></span></div>",
        )
    
    def test_to_html_empty_leaf(self):
        grandchild_node = LeafNode(None, "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span>grandchild</span></div>",
        )
    
    def test_to_html_props(self):
        props = {"href": "https://www.google.com","target": "_blank"}
        child_node = LeafNode("a", "google.com",props)
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            '''<div><a href="https://www.google.com" target="_blank">google.com</a></div>''',
        )

if __name__ == "__main__":
    unittest.main()