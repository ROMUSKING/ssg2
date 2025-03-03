import unittest

from leafnode import LeafNode
from textnode import TextNode, TextType


class TestLeafNode(unittest.TestCase):
    def test_error(self):        
        node = LeafNode("p", None)
        with self.assertRaises(                               ValueError):
            node.to_html()

    def test_error1(self):        
        with self.assertRaises(TypeError):
            LeafNode("p", "This is a HTML node", None, None)

    def test_neq(self):
        node = LeafNode("p", "This is a HTML node", {})
        node2 = LeafNode("p", "This is a HTML node")
        self.assertNotEqual(node, node2)


    def test_eq(self):
        node = LeafNode("p", "This is a paragraph node")
        html = "<p>This is a paragraph node</p>"
        self.assertEqual(node.to_html(), html)

    def test_eq1(self):
        node = LeafNode("p", "This is a HTML node", props={"background-image" : "/assets/image.jpg"})
        node2 = LeafNode("p", "This is a HTML node", {"background-image" : "/assets/image.jpg"})
        self.assertEqual(node, node2)

    def test_raw_repr(self):
        node = LeafNode(None,
                        ' background-image="/assets/image.jpg" width="100%"', 
                        props={
                            "background-image" : "/assets/image.jpg", 
                            "width" : "100%"
                            }
                        )
        raw = ' background-image="/assets/image.jpg" width="100%"'
        self.assertEqual(node.to_html(), raw)
        
    def test_from_text_node_bold(self):
        text_node = TextNode("This is a text node", TextType.BOLD)
        node = LeafNode(None, None)
        node2 = LeafNode("b", "This is a text node")
        node.from_text_node(text_node)
        self.assertEqual(node, node2)

    def test_from_text_node_image(self):
        text_node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev/_nuxt/9.B-zPuvyH.png")
        node = LeafNode(None, None)
        node.from_text_node(text_node)
        html = '<img src="https://www.boot.dev/_nuxt/9.B-zPuvyH.png" alt="This is an image">'
        self.assertEqual(node.to_html(), html)


    def test_from_text_node_link(self):
        text_node = TextNode("This is an link", TextType.LINK, "https://www.boot.dev/_nuxt/9.B-zPuvyH.png")
        node = LeafNode(None, None)
        node.from_text_node(text_node)
        
        html = '<a href="https://www.boot.dev/_nuxt/9.B-zPuvyH.png">This is an link</a>'
        self.assertEqual(node.to_html(), html)


    def test_from_text_node_italics(self):
        text_node = TextNode("This is an italical text", TextType.ITALIC, "https://www.boot.dev/_nuxt/9.B-zPuvyH.png")
        node = LeafNode(None, None)
        node.from_text_node(text_node)
        
        html = '<i>This is an italical text</i>'
        self.assertEqual(node.to_html(), html)


    def test_from_text_node_code(self):
        text_node = TextNode("This is an code", TextType.CODE, "https://www.boot.dev/_nuxt/9.B-zPuvyH.png")
        node = LeafNode(None, None)
        node.from_text_node(text_node)
        
        html = '<code>This is an code</code>'
        self.assertEqual(node.to_html(), html)



if __name__ == "__main__":
    unittest.main()
    
    
    