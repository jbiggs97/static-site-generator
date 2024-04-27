import unittest
from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode

class TestHTMLNode(unittest.TestCase):

    def test_propstohtml_str(self):
        node = HTMLNode()
        node.props = {"href": "https://www.google.com", "target": "_blank"}
        output = node.props_to_html()
        self.assertIsInstance(output, str)

    def test_propstohtml_count(self):
        node = HTMLNode()
        node.props = {"href": "https://www.google.com", "target": "_blank", "desc": "dummydesc"}
        output = node.props_to_html()
        output_properties_count = output.count("=")
        props_key_count = len(node.props)
        self.assertEqual(output_properties_count, props_key_count)

    def test_propstohtml_invalid(self):
        node = HTMLNode()
        node.props = None
        self.assertEqual(node.props_to_html(), "")

    def test_leafnode_value(self):
        node = LeafNode(None, None, None)
        self.assertRaises(ValueError, node.to_html)

    def test_leafnode_output(self):
        test_cases = [
            {
                'test': LeafNode('p', 'This is a paragraph of text.'),
                'expect': '<p>This is a paragraph of text.</p>'
            },
            {
                'test': LeafNode('a', 'Click me!', {'href': 'https://www.google.com'}),
                'expect': '<a href="https://www.google.com">Click me!</a>'
            },
            {
                'test': LeafNode('h1', 'My Header!'),
                'expect': '<h1>My Header!</h1>'
            }
        ]
        for case in test_cases:
            node = case["test"]
            output = node.to_html()
            self.assertEqual(output, case["expect"])

    def test_parent_recursion(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
