from enum import Enum

class TextTypes(Enum):
    BOLD = 1
    ITALIC = 2
    NORMAL = 3
    CODE = 4
    LINK = 5
    IMAGE = 6


class TextNode:
    def __init__(self, text, text_type, url=None) -> None:
        self.text = text
        self.text_type = text_type
        self.url = url

    
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
        return f"{class_name}({", ".join([str(x) for x in attributes])})"