from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, 
                 tag, 
                 children, 
                 props = None):
        super().__init__(                 
                 tag = tag, 
                 children = children, 
                 props = props)
        
    
    def __eq__(self, other):
        return (type(self) == type(other)            
            and self.tag == other.tag 
            and self.children == other.children 
            and self.props == other.props)
    
    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props_to_html()})"
    
    def to_html(self):
        if self.children is None or len(self.children) < 1:
            raise ValueError("All parent nodes must have children {duh!}")
        if self.tag is None or len(self.tag) < 1:
            raise ValueError("All parents must be tagged")
        children = ""
        for node in self.children:
            children += node.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children}</{self.tag}>"
