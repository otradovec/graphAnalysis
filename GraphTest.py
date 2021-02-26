import unittest
from Graph import Graph

class GraphTest(unittest.TestCase):
    def setUp(self):
        self.g = Graph(["A","B","C","D","E","F"])

    def test_add_node(self):
        self.assertTrue(self.g.has_node("A"))
        self.assertFalse(self.g.has_node("Z"))

    def test_add_not_oriented_connection(self):
        self.g.add_not_oriented_connection("A","B")
        self.assertTrue(self.g.is_connection("A","B"))
        self.assertTrue(self.g.is_connection("B","A"))
        self.assertFalse(self.g.is_connection("A","C"))
        with self.assertRaises(ValueError):
             self.g.add_not_oriented_connection("A","Z")

    def test_add_not_oriented_connections(self):
        self.g.add_not_oriented_connections([["A","B"],["B","C"],["D","E"]])
        self.assertTrue(self.g.is_connection("B","C"))
        self.assertTrue(self.g.is_connection("C","B"))
        self.assertFalse(self.g.is_connection("C","E"))

    def test_get_leaving_edges_size(self):
        self.g.add_not_oriented_connections([["A","B"],["B","C"],["D","E"]])
        self.g.print()
        self.assertEquals(1,self.g.get_leaving_edges_size("A"))
        self.assertEquals(2,self.g.get_leaving_edges_size("B"))
        self.assertEquals(1,self.g.get_leaving_edges_size("C"))
        self.assertEquals(0,self.g.get_leaving_edges_size("F"))




if __name__ == '__main__':
    unittest.main()
