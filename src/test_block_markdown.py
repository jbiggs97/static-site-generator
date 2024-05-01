import unittest

from block_markdown import (
    markdown_to_blocks
)
import main

class TestTextNode(unittest.TestCase):

    def test_markdown_to_blocks(self):
        test_cases = [
            {
                'test': "This is **bolded** paragraph\n\nThis is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line\n\n* This is a list\n* with items",
                'expect': [
                        'This is **bolded** paragraph',
                        'This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line',
                        '* This is a list\n* with items'
                        ]

            },
            {
                'test': "\n\nThis is **bolded** paragraph\n\n\n   This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line\n\n* This is a list\n* with items\n\n",
                'expect': [
                        'This is **bolded** paragraph',
                        'This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line',
                        '* This is a list\n* with items'
                        ]

            }

        ]
        for case in test_cases:
            blocks = markdown_to_blocks(case['test'])
            for index, block in enumerate(blocks):
                self.assertEqual(block, case["expect"][index])


if __name__ == "__main__":
    unittest.main()