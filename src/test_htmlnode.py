import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p",
                        "this is a value",
                        None,
                        {"href": "https://www.google.com", "target": "_blank"}
                        )
        print(node)
        node.props_to_html()
        print(node.props_to_html())

    def test_eq2(self):
        node = HTMLNode("p",
                        "this is a value",
                        None,
                        {"href": "https://www.bing.com", "target": "_gpt"}
                        )
        print(node)
        node.props_to_html()
        print(node.props_to_html())

    def test_eq3(self):
        node = HTMLNode(
                "p",
                "this is a value",
                None,
                {
                    "href": "https://www.armstrong.com",
                    "target": "_mgs",
                    "source": "i_made_it_up"
                }
            )
        print(node)
        node.props_to_html()
        print(node.props_to_html())

    def test_eq_leaf(self):
        node = LeafNode(
                "p",
                "Welcome to the backend, where the fun happens!",
                None
            )
        print(node.to_html())

    def test_eq_leaf2(self):
        node = LeafNode(
                "a",
                "Join us",
                {"href": "https://www.boot.dev"}
            )
        print(node.to_html())


if __name__ == "__main__":
    unittest.main()
