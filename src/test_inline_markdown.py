from textnode import TextNode, TextTypes
import unittest
from inline_markdown import (
    extract_markdown_images,
    extract_markdown_links,
    text_to_textnodes
)


class TestInlineMarkdown(unittest.TestCase):

    def test_image_extraction(self):
        test_cases = [
            {
                'test': 'This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png)',
                'expect': [("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"), ("another", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/dfsdkjfd.png")]
            }
        ]
        for case in test_cases:
            output = extract_markdown_images(case["test"])
            self.assertEqual(output, case["expect"])


    def test_link_extraction(self):
        test_cases = [
            {
                'test': 'This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)',
                'expect': [("link", "https://www.example.com"), ("another", "https://www.example.com/another")]
            },
            {
                'test': 'This is text with another [link-example](https://www.example-links&20?data=query.com)',
                'expect': [("link-example", "https://www.example-links&20?data=query.com")]
            },
        ]
        for case in test_cases:
            output = extract_markdown_links(case["test"])
            self.assertEqual(output, case["expect"])

    
    def test_text_to_textnodes(self):
        test_cases = [
            {
                'test': 'This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://boot.dev)',
                'expect': [
                            TextNode("This is ", TextTypes.TEXT),
                            TextNode("text", TextTypes.BOLD),
                            TextNode(" with an ", TextTypes.TEXT),
                            TextNode("italic", TextTypes.ITALIC),
                            TextNode(" word and a ", TextTypes.TEXT),
                            TextNode("code block", TextTypes.CODE),
                            TextNode(" and an ", TextTypes.TEXT),
                            TextNode("image", TextTypes.IMAGE, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
                            TextNode(" and a ", TextTypes.TEXT),
                            TextNode("link", TextTypes.LINK, "https://boot.dev"),
                        ]

            }
        ]
        for case in test_cases:
            output = text_to_textnodes(case["test"])
            for index, node in enumerate(output):
                self.assertEqual(node, case["expect"][index])


if __name__ == "__main__":
    unittest.main()
