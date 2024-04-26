import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):

    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)


    def test_noteq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italic")
        self.assertNotEqual(node, node2)


    def test_urlnone(self):
        node = TextNode("dummy", "dummy")
        self.assertIsNone(node.url)


    def test_texttypes(self):
        pass


if __name__ == "__main__":
    unittest.main()