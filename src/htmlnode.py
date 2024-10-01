class HTMLNode:

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise Exception(NotImplementedError)

    def props_to_html(self):
        final_html = ""
        for attribute in self.props:
            final_html += (
                    " " + attribute + "=" + '"' + self.props[attribute] + '"'
                )
        return final_html

    def __repr__(self):
        return (
            f"HTMLNode({self.tag}, {self.value}, "
            f"{self.children}, {self.props})"
        )
