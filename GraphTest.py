import unittest
from Graph import Graph

class GraphTest(unittest.TestCase):

    def test_add_node(self):
        g = Graph(["A","B"])
        self.assertTrue(g.has_node("A"))
        self.assertFalse(g.has_node("C"))

    def test_add_not_oriented_connection(self):
        g = Graph(["A","B","C"])
        g.add_not_oriented_connection("A","B")
        self.assertTrue(g.is_connection("A","B"))
        self.assertTrue(g.is_connection("B","A"))
        self.assertFalse(g.is_connection("A","C"))
        with self.assertRaises(ValueError):
             g.add_not_oriented_connection("A","Z")


if __name__ == '__main__':
    unittest.main()
