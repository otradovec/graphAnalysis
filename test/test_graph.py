import unittest
from src.Graph import Graph
from src.Connection import Connection

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

    def test_get_degree(self):
        self.g.add_oriented_connections([["A","B"],["B","C"],["D","E"]])
        self.assertEqual(1,self.g.get_degree("A"))
        self.assertEqual(2,self.g.get_degree("B"))
        self.assertEqual(1,self.g.get_degree("C"))
        self.assertEqual(1,self.g.get_degree("D"))
        self.assertEqual(0,self.g.get_degree("F"))


    def test_get_node_with_highest_degree(self):
        self.g.add_oriented_connections([["A","B"],["B","C"],["F","E"]])
        self.assertEqual("B",self.g.get_node_with_highest_degree())
        self.g.add_oriented_connections([["B","A"],["D","E"]])
        self.assertEqual("B",self.g.get_node_with_highest_degree())
        self.g.add_oriented_connections([["D","A"],["A","E"]])
        self.assertEqual("A",self.g.get_node_with_highest_degree())

    def test_is_oriented(self):
        self.assertFalse(self.g.is_oriented())
        self.g.add_not_oriented_connections([["D","B"]])
        self.assertFalse(self.g.is_oriented())
        self.g.add_oriented_connections([["A","B"]])
        self.assertTrue(self.g.is_oriented())
        self.g.add_oriented_connections([["D","A"],["A","E"]])
        self.assertTrue(self.g.is_oriented())

    def test_is_multigraph(self):
        self.assertFalse(self.g.is_multigraph())
        self.g.add_oriented_connections([["A","B"],["B","C"],["F","E"]])
        self.assertFalse(self.g.is_multigraph())
        self.g.add_oriented_connections([["A","B"]])
        self.assertTrue(self.g.is_multigraph())

    def test_is_tree(self):
        self.assertFalse(self.g.is_tree())
        self.g.add_not_oriented_connections([["A","B"],["B","C"],["B","D"]])
        self.assertFalse(self.g.is_tree())
        self.g.add_not_oriented_connections([["D","E"],["E","F"]])
        self.assertTrue(self.g.is_tree())
        self.g.add_not_oriented_connections([["A","F"]])
        self.assertFalse(self.g.is_tree())

    def test_is_connected(self):
        self.assertFalse(self.g.is_connected())
        self.g.add_not_oriented_connections([["A","B"],["B","C"],["B","D"]])
        self.assertFalse(self.g.is_connected())
        self.g.add_not_oriented_connections([["D","E"],["E","F"]])
        self.assertTrue(self.g.is_connected())
        self.g.add_not_oriented_connections([["A","F"]])
        self.assertTrue(self.g.is_connected())


    def test_has_loop(self):
        self.assertFalse(self.g.has_loop())
        self.g.add_oriented_connections([["A","B"],["B","C"],["F","E"]])
        self.assertFalse(self.g.has_loop())
        self.g.add_oriented_connections([["A","A"]])
        self.assertTrue(self.g.has_loop())

    def test_has_connectivity(self):
        self.assertFalse(self.g.has_connectivity())
        self.g.add_not_oriented_connections([["A","B"],["B","C"],["F","E"]])
        self.assertFalse(self.g.has_connectivity())
        self.g.add_not_oriented_connections([["A","D"],["C","E"]])
        self.assertTrue(self.g.has_connectivity())

    def test_get_neighbors(self):
        self.g.add_not_oriented_connections([["A","B"],["B","C"],["D","E"]])
        self.assertEqual({"B"},self.g.get_neighbors("A"))
        self.assertEqual({"A","C"},self.g.get_neighbors("B"))
        self.assertEqual({"D"},self.g.get_neighbors("E"))

    def test_is_complete(self):
        self.assertFalse(self.g.is_complete())
        self.g.add_not_oriented_connections([["A","B"],["B","C"],["D","E"]])
        self.assertFalse(self.g.is_complete())
        import itertools
        for conn in itertools.product(["A","B","C","D","E","F"],repeat=2):
            self.g.add_not_oriented_connection(conn[0],conn[1])
        self.assertTrue(self.g.is_complete())

    def test_has_bidirectional_edge(self):
        self.assertFalse(self.g.has_bidirectional_edge())
        self.g.add_oriented_connections([["A","B"],["B","C"],["D","E"]])
        self.assertFalse(self.g.has_bidirectional_edge())
        self.g.add_oriented_connections([["B","A"]])
        self.assertTrue(self.g.has_bidirectional_edge())

    def test_is_bidirectional(self):
        self.g.add_oriented_connections([["A","B"],["B","A"],["B","C"],["D","E"]])
        self.assertFalse(self.g.is_bidirectional())
        self.g.add_oriented_connections([["C","B"],["E","D"]])
        self.assertTrue(self.g.is_bidirectional())

    def test_total_cost(self):
        self.assertEqual(0,self.g.total_cost())
        self.g.add_not_oriented_valued_connections([["A","B",1],["B","C",5],["B","D",4]])
        self.assertEqual(10,self.g.total_cost())
        self.g.add_not_oriented_valued_connections([["D","E",3],["E","F",2]])
        self.assertEqual(15,self.g.total_cost())

    def test_get_minimal_spanning_tree(self):
        self.g.add_not_oriented_valued_connections([["A","B",1],["B","C",2],["B","D",1],["D","E",4],["E","F",2],["A","F",10],["A","C",7]])
        h = self.g.get_minimal_spanning_tree(printing=False)
        self.assertEqual(5,len(h.connections))
        self.assertEqual(10,h.total_cost())

    def test_bridges(self):
        self.g.add_not_oriented_connections([["A","B"],["B","C"],["C","D"],["A","C"]])
        self.assertEqual([Connection("C","D",False)],self.g.bridges())

    def test_separating_set(self):
        self.g.add_not_oriented_connections([["A","B"],["B","C"],["C","D"],["A","C"],["C","E"]])
        self.assertEqual({"C","F"},self.g.separating_set())

    def test_build_avl_tree(self):
        self.g = Graph(set())
        #self.g.build_avl_tree([5,15,10])
        #self.assertEqual(2,len(self.g.connections))
        #self.assertTrue(self.g.is_connection(5,10))
        #self.assertTrue(self.g.is_connection(10,15))

    def test_all_nodes_have_equal_in_out_degree(self):
        self.assertTrue(self.g.all_nodes_have_equal_in_out_degree())
        self.g.add_oriented_connections([["A","B"],["B","C"],["C","D"]])
        self.assertFalse(self.g.all_nodes_have_equal_in_out_degree())
        self.g.add_oriented_connections([["D","A"]])
        self.assertTrue(self.g.all_nodes_have_equal_in_out_degree())

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
