import re
from enum import Enum
from textnode import TextNode, TextTypes, text_node_to_html_node
from htmlnode import HTMLNode, ParentNode, LeafNode
from inline_markdown import text_to_textnodes

class BlockTypes(Enum):
    PARAGRAPH = 1
    HEADING = 2
    CODE = 3
    QUOTE = 4
    UL = 5
    OL = 6
    

def markdown_to_blocks(markdown):
    blocks = []
    md_blocks = markdown.split("\n\n")
    for block in md_blocks:
        if block == "":
            continue
        else:
            blocks.append(block.strip())
    return blocks


def block_to_block_type(markdown_block):
    lines_count = len(markdown_block.split("\n"))

    heading_pattern = re.compile(r"^#+ ")
    
    quote_pattern = re.compile(r"^>|\n>")
    quote_lines_count = len(re.findall(quote_pattern, markdown_block))

    ul_pattern = re.compile(r"^[*-] |\n[*-] ")
    ul_lines_count = len(re.findall(ul_pattern, markdown_block))

    ol_pattern = re.compile(r"^[0-9]+. |\n[0-9]+. ")
    ol_lines_count = len(re.findall(ol_pattern, markdown_block))

    if re.search(heading_pattern, markdown_block):
        return BlockTypes.HEADING
    elif markdown_block.startswith("```") and markdown_block.endswith("```"):
        return BlockTypes.CODE
    elif lines_count == quote_lines_count:
        return BlockTypes.QUOTE
    elif lines_count == ul_lines_count:
        return BlockTypes.UL
    elif lines_count == ol_lines_count:
        return BlockTypes.OL
    else:
        return BlockTypes.PARAGRAPH
    

def markdown_to_block_html(markdown_block):
    block_type = block_to_block_type(markdown_block)
    if block_type == BlockTypes.HEADING:
        block_html = heading_block_to_html_node(markdown_block)
    elif block_type == BlockTypes.PARAGRAPH:
        block_html = paragraph_to_html_node(markdown_block)
    elif block_type == BlockTypes.CODE:
        block_html = code_block_to_html_node(markdown_block)
    elif block_type == BlockTypes.QUOTE:
        block_html = quote_block_to_html_node(markdown_block)
    elif block_type == BlockTypes.UL:
        block_html = ul_block_to_html_node(markdown_block)
    elif block_type == BlockTypes.OL:
        block_html = ol_block_to_html_node(markdown_block)
    else:
        raise Exception("MARKDOWN_TO_HTML ERROR: invalid markdown block type.")
    return block_html


def markdown_to_html(markdown):
    html_blocks = []
    markdown_blocks = markdown_to_blocks(markdown)
    for block in markdown_blocks:
        html_block = markdown_to_block_html(block)
        html_blocks.append(html_block)
    return "\n".join(html_blocks)
    

def block_children_to_html(markdown_block):
    text_nodes = text_to_textnodes(markdown_block)
    html_nodes = [text_node_to_html_node(node) for node in text_nodes]
    return html_nodes


def code_block_children_to_html(markdown_block):
    text_nodes = text_to_textnodes(markdown_block, code=1)
    html_nodes = [text_node_to_html_node(node) for node in text_nodes]
    return html_nodes


def paragraph_to_html_node(markdown_block):
    children_nodes = block_children_to_html(markdown_block)
    node = ParentNode("p", children_nodes)
    html_str = node.to_html()
    return html_str


def heading_block_to_html_node(markdown_block):
    html_str = ""
    heading_level = len(markdown_block.split()[0])
    heading_values = " ".join(markdown_block.split()[1:])
    if heading_level > 6 or heading_level < 1:
        raise Exception("HEADING BLOCK TO HTML ERROR: heading level out of bounds", heading_level)
    else:
        node = ParentNode(f"h{heading_level}", block_children_to_html(heading_values))
        html_str = node.to_html()
    return html_str


def code_block_to_html_node(markdown_block):
    markdown_block = markdown_block.strip("`")
    html_str = ""
    node = ParentNode(f"code", code_block_children_to_html(markdown_block))
    pre_node = ParentNode("pre", [node])
    html_str = pre_node.to_html()
    return html_str


def quote_block_to_html_node(markdown_block):
    html_str = ""
    markdown_lines = "\n".join([" ".join(x.split()[1:]) for x in markdown_block.split("\n")])
    node = ParentNode(f"blockquote", block_children_to_html(markdown_lines))
    html_str = node.to_html()
    return html_str


def ul_block_to_html_node(markdown_block):
    html_str = ""
    markdown_lines = [" ".join(x.split()[1:]) for x in markdown_block.split("\n")]
    li_nodes = [ParentNode("li", block_children_to_html(x)) for x in markdown_lines]
    ul_node = ParentNode(f"ul", li_nodes)
    html_str = ul_node.to_html()
    return html_str


def ol_block_to_html_node(markdown_block):
    html_str = ""
    markdown_lines = [" ".join(x.split()[1:]) for x in markdown_block.split("\n")]
    li_nodes = [ParentNode("li", block_children_to_html(x)) for x in markdown_lines]
    ul_node = ParentNode(f"ol", li_nodes)
    html_str = ul_node.to_html()
    return html_str


if __name__ == "__main__":
    md = "* This is my code block with a **BOLD** word!\n* This is a second list Item\n* This is a *third* list Item."


    # print(markdown_to_html(md))