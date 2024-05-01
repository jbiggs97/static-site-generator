import unittest

from textnode import TextNode, TextTypes
import main

class TestTextNode(unittest.TestCase):

    def test_eq(self):
        node = TextNode("This is a text node", TextTypes.TEXT)
        node2 = TextNode("This is a text node", TextTypes.TEXT)
        self.assertEqual(node, node2)

        node = TextNode("image", TextTypes.IMAGE, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png")
        node2 = TextNode("image", TextTypes.IMAGE, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png")
        self.assertEqual(node, node2)


    def test_noteq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italic")
        self.assertNotEqual(node, node2)


    def test_urlnone(self):
        node = TextNode("dummy", "dummy")
        self.assertIsNone(node.url)


if __name__ == "__main__":
    unittest.main()