import htmlnode
from enum import Enum

class TextTypes(Enum):
    BOLD = 1
    ITALIC = 2
    TEXT = 3
    CODE = 4
    LINK = 5
    IMAGE = 6



class TextNode:
    def __init__(self, text, text_type, url=None) -> None:
        self.text = text
        self.text_type = text_type
        self.url = url

    def validate_text_type(self):
        pass
    
    def __eq__(self, other):
        if isinstance(other, TextNode):
            for item in self.__dict__:
                try:
                    if self.__dict__[item] != other.__dict__[item]:
                        return False
                except KeyError:
                    return False
            return True
        return False
        

    def __repr__(self):
        class_name = self.__class__.__name__
        attributes = list(self.__dict__.values())
        return f'{class_name}({", ".join([str(x) for x in attributes])})'
    


def text_node_to_html_node(text_node: TextNode):
    if text_node.text_type == TextTypes.TEXT:
        return htmlnode.LeafNode(None, text_node.text)
    elif text_node.text_type == TextTypes.BOLD:
        return htmlnode.LeafNode("b", text_node.text)
    elif text_node.text_type == TextTypes.ITALIC:
        return htmlnode.LeafNode("i", text_node.text)
    elif text_node.text_type == TextTypes.CODE:
        return htmlnode.LeafNode("code", text_node.text)
    elif text_node.text_type == TextTypes.LINK:
        return htmlnode.LeafNode("a", text_node.text, {"href": text_node.url})
    elif text_node.text_type == TextTypes.IMAGE:
        return htmlnode.LeafNode("img", text_node.text, {"href": text_node.url})
    else:
        raise Exception("TEXT_TYPE ERROR: Unknown text type.")