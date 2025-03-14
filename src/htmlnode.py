class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("not yet implemented")

    def props_to_html(self):
        if self.props is None:
            return ""
        props_str = ""
        for prop in self.props:
            props_str += f' {prop}="{self.props[prop]}"'
        return props_str

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.tag is None:
            return self.value
        tag_props = self.props_to_html()
        return f"<{self.tag}{tag_props}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("None tag arg is not valid")
        if not self.children or self.children is None:
            raise ValueError("None or empty children arg is not valid")

        html_str = ""
        for node in self.children:
            html_str += node.to_html()
        return f"<{self.tag}{self.props_to_html()}>{html_str}</{self.tag}>"
