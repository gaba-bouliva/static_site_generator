import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
      
    def test_repr_bold(self):
        node = TextNode("hello", TextType.BOLD, "https://example.com")
        self.assertEqual(repr(node), "Textnode(HELLO, BOLD, HTTPS://EXAMPLE.COM)")


      
    def test_repr_italic(self):
        node = TextNode("hello", TextType.ITALIC, "https://example.com")
        self.assertEqual(repr(node), "Textnode(hello, italic, https://example.com)")
    
    def test_init_invalid_text_type(self):
        with self.assertRaises(Exception):
            TextNode("hello", "invalid text type", "https://example.com")


    def test_repr_invalid_text_type(self):
        node = TextNode("hello", TextType.BOLD, "https://example.com")
        node.text_type = "invalid"
        with self.assertRaises(Exception):
            repr(node)

if __name__ == "__main__":
    unittest.main()