import unittest

from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html(self):
        node = HTMLNode()
        with self.assertRaises(NotImplementedError):
          node.to_html()
      
    def test_props_to_html(self):
        node = HTMLNode(props={ "href": "http://example.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), "href=\"http://example.com\" target=\"_blank\"")

    def test_repr_html_node(self):
        node = HTMLNode(tag="p", value="example paragraph", props={ "href": "http://example.com", "target": "_blank"})
        self.assertEqual(repr(node), "HTMLNode( tag: p, value: example paragraph, children: None, props: {'href': 'http://example.com', 'target': '_blank'})")
    
    def test_leaf_node_to_html_without_props(self):
        leaf = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(leaf.to_html(), "<p>This is a paragraph of text.</p>")
    
    def test_to_leaf_node_html_with_props(self):
        leaf = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(leaf.to_html(), "<a href=\"https://www.google.com\">Click me!</a>")
    
    def test_parent_node_to_html(self):
        parenNode = ParentNode("p",[
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],)
        self.assertEqual(parenNode.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")
