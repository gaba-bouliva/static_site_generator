import unittest

from textnode import TextNode, TextType
from htmlnode import HTMLNode


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
    