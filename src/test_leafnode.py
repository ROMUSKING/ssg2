import unittest

from leafnode import LeafNode


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


if __name__ == "__main__":
    unittest.main()