
class HTMLNode:
    def __init__(self, 
                 tag = None, 
                 value = None, 
                 children = None, 
                 props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def __eq__(self, other):
        return (type(self) == type(other)       
            and self.tag == other.tag 
                and self.value == other.value 
                and self.children == other.children 
                and self.props == other.props)
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props_to_html()})"
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        attr = ""
        if isinstance(self.props, dict) and len(self.props) > 0:                
            for k, v in self.props.items():
                attr += f' {k}="{v}"'        
        return attr

    def from_text_node(self, text_node):        
        raise NotImplementedError