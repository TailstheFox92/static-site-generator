import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode()
        self.props_to_html(node)


if __name__ == "__main__":
    unittest.main()
