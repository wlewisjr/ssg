import unittest

from htmlnode import LeafNode, ParentNode


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_great_grandchildren(self):
        great_grandchild_node = LeafNode("b", "great grandchild")
        grandchild_node = ParentNode("span", [great_grandchild_node])
        child_node = ParentNode("div", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><div><span><b>great grandchild</b></span></div></div>",
        )

    def test_to_html_with_multi_children(self):
        child_node = LeafNode("b", "child node")
        raw_text = LeafNode(None, "just some text")
        child_node2 = LeafNode(
            "a", "Boot.dev", {"href": "https://www.boot.dev", "target": "_blank"}
        )
        parent_node = ParentNode("div", [child_node, raw_text, child_node2])
        self.assertEqual(
            parent_node.to_html(),
            (
                "<div><b>child node</b>just some text"
                '<a href="https://www.boot.dev" target="_blank">Boot.dev</a></div>'
            ),
        )

    def test_to_html_parent_node_props(self):
        child_node = LeafNode("b", "child node")
        parent_node = ParentNode("div", [child_node], {"class": "pretty"})
        self.assertEqual(
            parent_node.to_html(), '<div class="pretty"><b>child node</b></div>'
        )


if __name__ == "__main__":
    unittest.main()
