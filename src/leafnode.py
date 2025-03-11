from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.tag is None:
            return self.value
        tag_props = self.props_to_html()
        return f"<{self.tag}{tag_props}>{self.value}</{self.tag}>"
