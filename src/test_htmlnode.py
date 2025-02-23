import unittest

from htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "This is a HTML node", None, None)
        node2 = HTMLNode("p", "This is a HTML node")
        self.assertEqual(node, node2)

    def test_neq(self):
        node = HTMLNode("p", "This is a HTML node", None, {})
        node2 = HTMLNode("p", "This is a HTML node")
        self.assertNotEqual(node, node2)


    def test_eq1(self):
        node = HTMLNode("p", "This is a paragraph node")
        node2 = HTMLNode("p", "This is a paragraph node")
        node3 = HTMLNode("p", "This is a paragraph node")
        node4 = HTMLNode("div", "This is a DIV node", [node, node2, node3], {"width" : "100%"})
        node5 = HTMLNode(tag="div", 
                         value="This is a DIV node",
                         children=[
                             HTMLNode("p", "This is a paragraph node"),
                             HTMLNode("p", "This is a paragraph node"),
                             HTMLNode("p", "This is a paragraph node")], 
                         props={"width" : "100%"}
                         )        
        self.assertEqual(node4, node5)

    def test_neq1(self):
        node = HTMLNode("p", "This is a HTML node", props={"background-image" : "/assets/image.jpg"})
        node2 = HTMLNode("p", "This is a HTML node", {"background-image" : "/assets/image.jpg"})
        self.assertNotEqual(node, node2)

    def test_prop_repr(self):
        node = HTMLNode("p", 
                        "This is a HTML node", 
                        props={
                            "background-image" : "/assets/image.jpg", 
                            "width" : "100%"
                            }
                        )
        props = ' background-image="/assets/image.jpg" width="100%"'
        self.assertEqual(node.props_to_html(), props)


if __name__ == "__main__":
    unittest.main()