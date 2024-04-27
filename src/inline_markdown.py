from textnode import TextNode, TextTypes
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        split_strings = node.text.split(delimiter)
        for index, s in enumerate(split_strings):
            if s == "":
                continue
            elif index % 2 == 1 and s != "":
                new_node = TextNode(s, text_type)
                new_nodes.append(new_node)
            else:
                new_node = TextNode(s, TextTypes.TEXT)
                new_nodes.append(new_node)
    return new_nodes


def extract_markdown_images(text):
    pattern = re.compile(r"!\[(.*?)\]\((.*?)\)", re.IGNORECASE)
    matches = re.findall(pattern, text)
    return matches


def extract_markdown_links(text):
    pattern = re.compile(r"\[(.*?)\]\((.*?)\)", re.IGNORECASE)
    matches = re.findall(pattern, text)
    return matches


if __name__ == "__main__":
    # nodes = [
    #     TextNode("`Starting` This is text with a **bold word** and a `code block` word and a `second block` word.", TextTypes.TEXT),
    #     TextNode("nextnode", TextTypes.TEXT),
    #     # TextNode("third", TextTypes.TEXT),
    #     # TextNode("fourth", TextTypes.TEXT),
    #     # TextNode("fifth", TextTypes.TEXT)
    # ]

    # print(split_nodes_delimiter(nodes, "`", TextTypes.CODE))
    text1 = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
    print(extract_markdown_images(text1))

    text2 = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
    print(extract_markdown_links(text2))
