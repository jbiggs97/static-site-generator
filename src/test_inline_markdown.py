import unittest
from inline_markdown import (
    extract_markdown_images,
    extract_markdown_links
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


if __name__ == "__main__":
    unittest.main()
