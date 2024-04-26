from textnode import TextNode

tn = TextNode("This is a text node", "Bold", "url.com")
tn2 = TextNode("This is a text node", "Bold")

print(tn.__eq__(tn2))