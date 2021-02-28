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

    def test_add_oriented_connection(self):
        self.assertFalse(self.g.is_connection("A","B"))
        self.g.add_oriented_connection("A","B")
        self.assertTrue(self.g.is_connection("A","B"))
        self.assertFalse(self.g.is_connection("D","E"))
        self.g.add_oriented_connection("D","E")
        self.assertTrue(self.g.is_connection("D","E"))

    def test_add_oriented_connections(self):
        self.g.add_oriented_connections([["A","B"],["C","B"],["F","E"]])
        self.assertFalse(self.g.is_connection("B","C"))
        self.assertTrue(self.g.is_connection("C","B"))
        self.assertFalse(self.g.is_connection("C","E"))
        self.assertTrue(self.g.is_connection("F","E"))

    def test_add_not_oriented_connections(self):
        self.g.add_not_oriented_connections([["A","B"],["B","C"],["D","E"]])
        self.assertTrue(self.g.is_connection("B","C"))
        self.assertTrue(self.g.is_connection("C","B"))
        self.assertFalse(self.g.is_connection("C","E"))

    def test_get_leaving_edges_size(self):
        self.g.add_not_oriented_connections([["A","B"],["B","C"],["D","E"]])
        self.assertEqual(1,self.g.get_leaving_edges_size("A"))
        self.assertEqual(2,self.g.get_leaving_edges_size("B"))
        self.assertEqual(1,self.g.get_leaving_edges_size("C"))
        self.assertEqual(0,self.g.get_leaving_edges_size("F"))

    def test_get_neighbors(self):
        self.g.add_not_oriented_connections([["A","B"],["B","C"],["D","E"]])
        self.assertEqual({"B"},self.g.get_neighbors("A"))
        self.assertEqual({"A","C"},self.g.get_neighbors("B"))
        self.assertEqual({"D"},self.g.get_neighbors("E"))


    def test_get_num_of_unique_neigbors(self):
        self.g.add_not_oriented_connections([["A","B"],["B","C"],["D","E"]])
        self.assertEqual(1,self.g.get_num_of_unique_neigbors({"A"}))
        self.assertEqual(0,self.g.get_num_of_unique_neigbors({"F"}))
        self.assertEqual(2,self.g.get_num_of_unique_neigbors({"B"}))
        self.assertEqual(2,self.g.get_num_of_unique_neigbors({"A","D"}))
        self.assertEqual(2,self.g.get_num_of_unique_neigbors({"A","B","D"}))

    def test_get_three_node_combinations_without_repetition(self):
        self.assertEqual(20,len(self.g.get_three_node_combinations_without_repetition()))

    def test_get_three_nodes_with_most_unique_neigbors(self):
        self.g.add_not_oriented_connections([["A","B"],["B","C"],["D","E"]])
        self.assertTrue({"B","D","F"} == self.g.get_three_nodes_with_most_unique_neigbors() or {"B","E","F"} ==  self.g.get_three_nodes_with_most_unique_neigbors())

    def test_nodes_as_str(self):
        self.assertEqual("A, B, C",self.g.nodes_as_str(['A',"B","C"]))

if __name__ == '__main__':
    unittest.main()
