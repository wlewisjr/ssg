import unittest

from htmlnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node_props = {
            "href": "https://www.boot.dev",
            "target": "_blank"
        }
        node = LeafNode("a", "Boot.dev", node_props)
        html_tag = '<a href="https://www.boot.dev" target="_blank">Boot.dev</a>'
        self.assertEqual(node.to_html(), html_tag)

    def test_leaf_to_html_notag(self):
        node = LeafNode(None, "Just some text")
        self.assertEqual(node.to_html(), "Just some text")

    def test_leaf_to_html_notag_props(self):
        node_props = {
            "href": "https://www.boot.dev",
            "target": "_blank"
        }
        node = LeafNode(None, "Just some text", node_props)
        self.assertEqual(node.to_html(), "Just some text")


if __name__ == "__main__":
    unittest.main()
