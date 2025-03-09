import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.BOLD, "http://something.com")
        t_repr = "TextNode(This is a text node, bold, http://something.com)"
        self.assertEqual(repr(node), t_repr)

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.LINK, "http://something.com")
        node2 = TextNode("This is a text node", TextType.LINK, "http://something.com")
        self.assertEqual(node, node2)

    def test_neq_text(self):
        node = TextNode("This is a text node", TextType.LINK, "http://something.com")
        t_repr = "TextNode(this is a text node, link, http://something.com)"
        self.assertNotEqual(repr(node), t_repr)

    def test_neq_type(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
