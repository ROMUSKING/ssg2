import unittest

from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_error(self):        
        node = ParentNode("p", None)
        with self.assertRaises(                               ValueError):
            node.to_html()
            
    def test_error00(self):        
        node = ParentNode("p", [])
        with self.assertRaises(                               ValueError):
            node.to_html()
            
    def test_error0(self):        
        node = ParentNode(None, [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ])
        with self.assertRaises(                               ValueError):
            node.to_html()

    def test_error1(self):        
        with self.assertRaises(TypeError):
            ParentNode("p", value="This is a HTML node")


    def test_eq(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )     
       
        html = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(node.to_html(), html)


    def test_eq1(self):
        node = ParentNode(
            "div",
            [ParentNode("p",
                [
                    LeafNode("b", "Bold text"),
                    LeafNode(None, "Normal text"),
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text"),
                ]
                )
             ]
            )     
        
        html = "<div><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p></div>"
        self.assertEqual(node.to_html(), html)


if __name__ == "__main__":
    unittest.main()
    
    