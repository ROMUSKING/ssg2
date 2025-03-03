from htmlnode import HTMLNode
from textnode import TextNode, TextType


class LeafNode(HTMLNode):
    def __init__(self, 
                 tag, 
                 value, 
                 props = None):
        super().__init__(                 
                 tag = tag, 
                 value = value, 
                 props = props)
        
    
    def __eq__(self, other):
        return (type(self) == type(other)            
            and self.tag == other.tag 
            and self.value == other.value 
            and self.props == other.props)
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props_to_html()})"
    
    def to_html(self):
        if self.value is None :
            raise ValueError("All leaf nodes must have a value")
        if self.tag is None or len(self.tag) < 1:
            return self.value
        if len(self.value) < 1:
            return f"<{self.tag}{self.props_to_html()}>"
                    
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        
    def from_text_node(self, text_node):
        if not isinstance(text_node, TextNode):
           raise TypeError(f"whatcha doin giving me this {type(text_node)}?") 
              
        match text_node.text_type:
            case TextType.TEXT:
                self.__init__(tag=None,
                    value = text_node.text)
            case TextType.BOLD:
                self.__init__(tag = "b",
                    value = text_node.text)
            case TextType.ITALIC:
                self.__init__(tag = "i",
                    value = text_node.text)
            case TextType.CODE:
                self.__init__(tag = "code",
                    value = text_node.text)
            case TextType.LINK:
                self.__init__(tag = "a",
                    value = text_node.text,
                    props = {"href": text_node.url})
            case TextType.IMAGE:
                self.__init__(tag = "img",
                    value = "",
                    props = {"src" : text_node.url, "alt" : text_node.text})
            case _:
                raise ValueError("what the heck is this?")