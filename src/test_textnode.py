import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_eq2(self):
        node = TextNode("This is a text node", "italic")
        node2 = TextNode("This is a text node", "italic")
        self.assertEqual(node, node2)

    def test_eq3(self):
        node = TextNode("This is a text node 2 electric boogaloo", "bold")
        node2 = TextNode("This is a text node 2 electric boogaloo", "bold")
        self.assertEqual(node, node2)

    def test_eq4(self):
        node = TextNode(1, 2)
        node2 = TextNode(1, 2)
        self.assertEqual(node, node2)

    def test_eq5(self):
        node = TextNode("This is a text node", "bold", None)
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
