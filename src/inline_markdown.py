from textnode import TextNode, TextTypes
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextTypes.TEXT:
            new_nodes.append(node)
            continue
        working_text = node.text
        split_strings = working_text.split(delimiter)
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


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        images = extract_markdown_images(node.text)
        if images == []:
            new_nodes.append(node)
            continue
        original_text = node.text
        for image in images:
            split_strings = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if split_strings[0] != "":
                txt_node = TextNode(split_strings[0], TextTypes.TEXT)
                new_nodes.append(txt_node)
            img_node = TextNode(image[0], TextTypes.IMAGE, image[1])
            new_nodes.append(img_node)
            original_text = split_strings[1]
            if image == images[-1] and split_strings[1] != "":
                txt_node = TextNode(split_strings[1], TextTypes.TEXT)
                new_nodes.append(txt_node)
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        links = extract_markdown_links(node.text)
        if links == []:
            new_nodes.append(node)
            continue
        original_text = node.text
        for link in links:
            split_strings = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if split_strings[0] != "":
                txt_node = TextNode(split_strings[0], TextTypes.TEXT)
                new_nodes.append(txt_node)
            lnk_node = TextNode(link[0], TextTypes.LINK, link[1])
            new_nodes.append(lnk_node)
            original_text = split_strings[1]
            if link == links[-1] and split_strings[1] != "":
                txt_node = TextNode(split_strings[1], TextTypes.TEXT)
                new_nodes.append(txt_node)
    return new_nodes


def text_to_textnodes(text, code=0):
    nodes = [TextNode(text, TextTypes.TEXT)]
    if code == 1:
        return nodes
    nodes = (split_nodes_delimiter(nodes, "**", text_type=TextTypes.BOLD))
    nodes = (split_nodes_delimiter(nodes, "*", text_type=TextTypes.ITALIC))
    nodes = (split_nodes_delimiter(nodes, "`", text_type=TextTypes.CODE))
    nodes = (split_nodes_image(nodes))
    nodes = (split_nodes_link(nodes))
    return nodes


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
    # text1 = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)"
    # print(extract_markdown_images(text1))

    # text2 = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
    # print(extract_markdown_links(text2))

    # node = TextNode(
    #     "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)",
    #     TextTypes.TEXT,
    # )

    text = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)"

    # print(text_to_textnodes(text))