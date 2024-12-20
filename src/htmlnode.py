class HTMLNode:

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        if not self.props:
            raise ValueError("Invalid HTML: no properties")
        final_html = ""
        for attribute in self.props:
            final_html += (
                    " " + attribute + "=" + '"' + self.props[attribute] + '"'
                )
        return final_html

    def __repr__(self):
        return (
                f"HTMLNode({self.tag}, {self.value}, "
                f"children: {self.children}, {self.props})"
        )


class LeafNode(HTMLNode):

    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.value:
            raise ValueError("Invalid HTML: no value")
        if not self.tag:
            return self.value
        if self.props:
            return (
                    f"<{self.tag}"
                    f"{self.props_to_html()}>"
                    f"{self.value}"
                    f"</{self.tag}>"
                )
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"


class ParentNode(HTMLNode):

    def __init__(self, tag, children):
        super().__init__(tag, None, children, None)
    
    def to_html(self):
        if not self.tag:
            raise ValueError("Invalid HTML: no value")
        if not self.children:
            raise ValueError("Invalid HTML: no children")
        final_html = ""
        for node in self.children:
            final_html += node.to_html()
        return f"<{self.tag}>{final_html}</{self.tag}>"
