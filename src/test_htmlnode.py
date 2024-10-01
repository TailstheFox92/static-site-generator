import unittest

from htmlnode import HTMLNode


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


if __name__ == "__main__":
    unittest.main()
