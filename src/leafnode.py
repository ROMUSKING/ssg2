from htmlnode import HTMLNode


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
        if self.value is None or len(self.value) < 1:
            raise ValueError("All leaf nodes must have a value")
        if self.tag is None or len(self.tag) < 1:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
