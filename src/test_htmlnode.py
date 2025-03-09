import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node_props = {
            "href": "https://www.boot.dev",
            "target": "_blank",
        }
        node = HTMLNode("a", "Boot.dev", None, node_props)
        props_str = ' href="https://www.boot.dev" target="_blank"'
        self.assertEqual(node.props_to_html(), props_str)

    def test_attributes(self):
        node = HTMLNode("p", "This is a paragraph.")
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "This is a paragraph.")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)

    def test_repr(self):
        node_props = {
            "src": "pepe.gif",
            "alt": "pepe",
        }
        node = HTMLNode("img", None, None, node_props)
        repr_str = f"HTMLNode(img, None, None, {node_props})"
        self.assertEqual(repr(node), repr_str)


if __name__ == "__main__":
    unittest.main()
