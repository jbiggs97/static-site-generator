class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("Not implemented.")
    
    def props_to_html(self):
        return_str = ""
        if isinstance(self.props, dict):
            for item in self.props:
                return_str += f' {item}="{self.props[item]}"'
        return return_str
    

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None) -> None:
        super().__init__(tag, value, None, props)

    def to_html(self) -> str:
        if self.value is None:
            raise ValueError(f"No value in :{self}")
        elif self.tag is None:
            return str(self.value)
        else:
            if self.tag in {'img'}:
                props_str = self.props_to_html()
                return f"<{self.tag}{props_str}>{self.value}"
            else:
                props_str = self.props_to_html()
                return f"<{self.tag}{props_str}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None) -> None:
        super().__init__(tag, None, children, props)
        

    def to_html(self):
        html_str = ""
        if self.tag is None:
            raise ValueError("No tag provided")
        elif self.children is None:
            raise ValueError("No children provided")
        else:
            props_str = self.props_to_html()
            inner_html = ""
            for child in self.children:
                inner_html += child.to_html()
                html_str = f"<{self.tag}{props_str}>{inner_html}</{self.tag}>" #+ self.to_html()
            return html_str