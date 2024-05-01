from textnode import TextNode

import re

pattern = re.compile(r"[0-9]+. |\n[0-9]+. ")

text = "0. Hello World\n1. this is a quote\n11. this is a second quote"
lines = len(text.split("\n"))

quote_new_lines = len(re.findall(pattern, text))

print(lines, quote_new_lines, lines == quote_new_lines)