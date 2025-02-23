import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_neq(self):
        node = TextNode("This is a text node", TextType.BOLD, "http://cknik.uk")
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)


    def test_eq1(self):
        node = TextNode("This is a text node", TextType.TEXT, "http://cknik.uk")
        node2 = TextNode("This is a text node", TextType.TEXT, "http://cknik.uk")
        self.assertEqual(node, node2)

    def test_neq1(self):
        node = TextNode("This is a text node", TextType.BOLD, "http://cknik.uk")
        node2 = TextNode("This is a text node", TextType.ITALIC, "http://cknik.uk")
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()