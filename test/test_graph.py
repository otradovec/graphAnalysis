import unittest
from unittest import TestCase

from src.Graph import Graph
from src.Connection import Connection
from src.Node import Node


class GraphTest(unittest.TestCase):
    def setUp(self):
        self.g = Graph(["A", "B", "C", "D", "E", "F"])

    def test_get_node(self):
        self.assertEqual(self.g.get_node("A").name, "A")
        self.assertEqual(self.g.get_node("A").name, "A")
        self.assertEqual(self.g.get_node("B").name, "B")
        self.assertIsNone(self.g.get_node("Z"))

    def test_add_node(self):
        self.assertTrue(self.g.has_node("A"))
        self.assertFalse(self.g.has_node("Z"))

    def test_has_node(self):
        self.assertTrue(self.g.has_node("A"))
        self.assertTrue(self.g.has_node(Node("A").name))

    def test_add_not_oriented_connection(self):
        self.g.add_not_oriented_connection(Node("A"), Node("B"))
        self.assertTrue(self.g.is_connection("A", "B"))
        self.assertTrue(self.g.is_connection("B", "A"))
        self.assertFalse(self.g.is_connection("A", "C"))
        with self.assertRaises(ValueError):
            self.g.add_not_oriented_connection(Node("A"), Node("Z"))

    def test_add_oriented_connection(self):
        self.assertFalse(self.g.is_connection("A", "B"))
        self.g.add_oriented_connection("A", "B")
        self.assertTrue(self.g.is_connection("A", "B"))
        self.assertFalse(self.g.is_connection("D", "E"))
        self.g.add_oriented_connection("D", "E")
        self.assertTrue(self.g.is_connection("D", "E"))

    def test_add_oriented_connections(self):
        self.g.add_oriented_connections([["A", "B"], ["C", "B"], ["F", "E"]])
        self.assertFalse(self.g.is_connection("B", "C"))
        self.assertTrue(self.g.is_connection("C", "B"))
        self.assertFalse(self.g.is_connection("C", "E"))
        self.assertTrue(self.g.is_connection("F", "E"))

    def test_add_not_oriented_connections(self):
        self.g.add_not_oriented_connections([[Node("A"), Node("B")], [Node("B"), Node("C")], [Node("D"), Node("E")]])
        self.assertTrue(self.g.is_connection("B", "C"))
        self.assertTrue(self.g.is_connection("C", "B"))
        self.assertFalse(self.g.is_connection("C", "E"))

    def test_remove_node(self):
        self.g.add_not_oriented_connections([[Node("A"), Node("B")], [Node("B"), Node("C")], [Node("D"), Node("E")]])
        self.g.remove_node(Node("B"))
        self.assertEqual(5, len(self.g.nodes))
        self.assertEqual(1, len(self.g.connections))

    def test_get_leaving_edges_size(self):
        self.g.add_not_oriented_connections([["A", "B"], ["B", "C"], ["D", "E"]])
        self.assertEqual(1, self.g.get_leaving_edges_size(Node("A")))
        self.assertEqual(2, self.g.get_leaving_edges_size(Node("B")))
        self.assertEqual(1, self.g.get_leaving_edges_size(Node("C")))
        self.assertEqual(0, self.g.get_leaving_edges_size(Node("F")))
        self.g.add_oriented_connections([["C", "A"]])
        self.assertEqual(1, self.g.get_leaving_edges_size(Node("A")))
        self.assertEqual(2, self.g.get_leaving_edges_size(Node("B")))
        self.assertEqual(2, self.g.get_leaving_edges_size(Node("C")))
        self.assertEqual(0, self.g.get_leaving_edges_size(Node("F")))

    def test_get_degree(self):
        self.g.add_oriented_connections([["A", "B"], ["B", "C"], ["D", "E"]])
        self.assertEqual(1, self.g.get_degree(Node("A")))
        self.assertEqual(2, self.g.get_degree(Node("B")))
        self.assertEqual(1, self.g.get_degree(Node("C")))
        self.assertEqual(1, self.g.get_degree(Node("D")))
        self.assertEqual(0, self.g.get_degree(Node("F")))

    def test_get_node_with_highest_degree(self):
        self.g.add_oriented_connections([["A", "B"], ["B", "C"], ["F", "E"]])
        self.assertEqual(Node("B"), self.g.get_node_with_highest_degree())
        self.g.add_oriented_connections([["B", "A"], ["D", "E"]])
        self.assertEqual(Node("B"), self.g.get_node_with_highest_degree())
        self.g.add_oriented_connections([["D", "A"], ["A", "E"]])
        self.assertEqual(Node("A"), self.g.get_node_with_highest_degree())

    def test_is_oriented(self):
        self.assertFalse(self.g.is_oriented())
        self.g.add_not_oriented_connections([["D", "B"]])
        self.assertFalse(self.g.is_oriented())
        self.g.add_oriented_connections([["A", "B"]])
        self.assertTrue(self.g.is_oriented())
        self.g.add_oriented_connections([["D", "A"], ["A", "E"]])
        self.assertTrue(self.g.is_oriented())

    def test_is_multigraph(self):
        self.assertFalse(self.g.is_multigraph())
        self.g.add_oriented_connections([["A", "B"], ["B", "C"], ["F", "E"]])
        self.assertFalse(self.g.is_multigraph())
        self.g.add_oriented_connections([["A", "B"]])
        self.assertTrue(self.g.is_multigraph())

    def test_is_tree(self):
        self.assertFalse(self.g.is_tree())
        self.g.add_not_oriented_connections([["A", "B"], ["B", "C"], ["B", "D"]])
        self.assertFalse(self.g.is_tree())
        self.g.add_not_oriented_connections([["D", "E"], ["E", "F"]])
        self.assertTrue(self.g.is_tree())
        self.g.add_not_oriented_connections([["A", "F"]])
        self.assertFalse(self.g.is_tree())

    def test_is_connected(self):
        self.assertFalse(self.g.is_connected())
        self.g.add_not_oriented_connections([["A", "B"], ["B", "C"], ["B", "D"]])
        self.assertFalse(self.g.is_connected())
        self.g.add_not_oriented_connections([["D", "E"], ["E", "F"]])
        self.assertTrue(self.g.is_connected())
        self.g.add_not_oriented_connections([["A", "F"]])
        self.assertTrue(self.g.is_connected())

    def test_has_loop(self):
        self.assertFalse(self.g.has_loop())
        self.g.add_oriented_connections([["A", "B"], ["B", "C"], ["F", "E"]])
        self.assertFalse(self.g.has_loop())
        self.g.add_oriented_connections([["A", "A"]])
        self.assertTrue(self.g.has_loop())

    def test_has_connectivity(self):
        self.assertFalse(self.g.has_connectivity())
        self.g.add_not_oriented_connections([["A", "B"], ["B", "C"], ["F", "E"]])
        self.assertFalse(self.g.has_connectivity())
        self.g.add_not_oriented_connections([["A", "D"], ["C", "E"]])
        self.assertTrue(self.g.has_connectivity())

    def test_reachable_nodes(self):
        self.assertEqual(1, len(self.g.reachable_nodes(Node("A"))))
        self.g.add_not_oriented_connections([["A", "B"], ["B", "C"], ["D", "E"]])
        self.assertEqual(3, len(self.g.reachable_nodes(Node("A"))))
        self.assertEqual(2, len(self.g.reachable_nodes(Node("D"))))
        self.assertEqual(1, len(self.g.reachable_nodes(Node("F"))))

    def test_get_neighbors(self):
        self.g.add_not_oriented_connections([["A", "B"], ["B", "C"], ["D", "E"]])
        self.assertEqual({Node("B")}, self.g.get_neighbors(Node("A")))
        self.assertEqual({Node("A"), Node("C")}, self.g.get_neighbors(Node("B")))
        self.assertEqual({Node("D")}, self.g.get_neighbors(Node("E")))

    def test_is_complete(self):
        self.assertFalse(self.g.is_complete())
        self.g.add_not_oriented_connections([["A", "B"], ["B", "C"], ["D", "E"]])
        self.assertFalse(self.g.is_complete())
        import itertools
        for conn in itertools.product(["A", "B", "C", "D", "E", "F"], repeat=2):
            self.g.add_not_oriented_connection(conn[0], conn[1])
        self.assertTrue(self.g.is_complete())

    def test_has_bidirectional_edge(self):
        self.assertFalse(self.g.has_bidirectional_edge())
        self.g.add_oriented_connections([["A", "B"], ["B", "C"], ["D", "E"]])
        self.assertFalse(self.g.has_bidirectional_edge())
        self.g.add_oriented_connections([["B", "A"]])
        self.assertTrue(self.g.has_bidirectional_edge())

    def test_is_bidirectional(self):
        self.g.add_oriented_connections([["A", "B"], ["B", "A"], ["B", "C"], ["D", "E"]])
        self.assertFalse(self.g.is_bidirectional())
        self.g.add_oriented_connections([["C", "B"], ["E", "D"]])
        self.assertTrue(self.g.is_bidirectional())

    def test_total_cost(self):
        self.assertEqual(0, self.g.total_cost())
        self.g.add_not_oriented_valued_connections([["A", "B", 1], ["B", "C", 5], ["B", "D", 4]])
        self.assertEqual(10, self.g.total_cost())
        self.g.add_not_oriented_valued_connections([["D", "E", 3], ["E", "F", 2]])
        self.assertEqual(15, self.g.total_cost())

    def test_get_minimal_spanning_tree(self):
        self.g.add_not_oriented_valued_connections(
            [["A", "B", 1], ["B", "C", 2], ["B", "D", 1], ["D", "E", 4], ["E", "F", 2], ["A", "F", 10], ["A", "C", 7]])
        h = self.g.get_minimal_spanning_tree(printing=False)
        self.assertEqual(5, len(h.connections))
        self.assertEqual(10, h.total_cost())

    def test_present_in_components(self):
        f = Graph({"A", "B"})
        f.add_not_oriented_connections([["A", "B"]])
        s = Graph({"C"})
        t = Graph({"D", "E", "F"})
        t.add_not_oriented_connections([["D", "E"], ["E", "F"]])
        self.assertTrue(self.g.present_in_components(f.get_node("A"), {f, s}))
        self.assertTrue(self.g.present_in_components(t.get_node("F"), {f, s, t}))
        self.assertFalse(self.g.present_in_components(t.get_node("F"), {f, s}))
        self.assertFalse(self.g.present_in_components(f.get_node("B"), {s, t}))
        self.assertFalse(self.g.present_in_components(f.get_node("B"), {t}))
        self.assertTrue(f.present_in_components(f.get_node("A"), {f}))

    def test_components(self):
        self.assertEqual(len(self.g.nodes), len(self.g.components()))
        self.g.add_not_oriented_connections([["A", "B"], ["B", "C"]])
        self.assertEqual(len(self.g.nodes) - 2, len(self.g.components()))

    def test_is_bridge(self):
        self.g.add_not_oriented_connections([["A", "B"], ["B", "C"], ["C", "D"], ["A", "C"]])
        self.assertFalse(self.g.is_bridge(Connection("A", "B", False)))
        self.assertTrue(self.g.is_bridge(Connection("C", "D", False)))

    def test_bridges(self):
        self.g.add_not_oriented_connections([["A", "B"], ["B", "C"], ["C", "D"], ["A", "C"]])
        self.assertEqual([Connection("C", "D", False)], self.g.bridges())

    def test_separating_set(self):
        self.g.add_not_oriented_connections([["A", "B"], ["B", "C"], ["C", "D"], ["A", "C"], ["C", "E"]])
        self.assertEqual({Node("C"), Node("F")}, self.g.separating_set())

    def test_build_avl_tree(self):
        self.g = Graph(set())
        # self.g.build_avl_tree([5,15,10])
        # self.assertEqual(2,len(self.g.connections))
        # self.assertTrue(self.g.is_connection(5,10))
        # self.assertTrue(self.g.is_connection(10,15))

    def test_get_incoming_degree(self):
        self.assertEqual(self.g.get_incoming_degree("A"), 0)
        self.g.add_oriented_connections([["A", "B"]])
        self.assertEqual(self.g.get_incoming_degree("A"), 0)
        self.assertEqual(self.g.get_incoming_degree("B"), 1)
        self.g.add_not_oriented_connections([["B", "C"]])
        self.assertEqual(self.g.get_incoming_degree("B"), 2)
        self.assertEqual(self.g.get_incoming_degree("C"), 1)

    def test_all_nodes_have_equal_in_out_degree(self):
        self.assertTrue(self.g.all_nodes_have_equal_in_out_degree())
        self.g.add_oriented_connections([["A", "B"], ["B", "C"], ["C", "D"]])
        self.assertFalse(self.g.all_nodes_have_equal_in_out_degree())
        self.g.add_oriented_connections([["D", "A"]])
        self.assertTrue(self.g.all_nodes_have_equal_in_out_degree())

    def test_get_num_of_unique_neigbors(self):
        self.g.add_not_oriented_connections([["A", "B"], ["B", "C"], ["D", "E"]])
        self.assertEqual(1, self.g.get_num_of_unique_neigbors({Node("A")}))
        self.assertEqual(0, self.g.get_num_of_unique_neigbors({Node("F")}))
        self.assertEqual(2, self.g.get_num_of_unique_neigbors({Node("B")}))
        self.assertEqual(2, self.g.get_num_of_unique_neigbors({Node("A"), Node("D")}))
        self.assertEqual(2, self.g.get_num_of_unique_neigbors({Node("A"), Node("B"), Node("D")}))

    def test_get_node_with_lowest_value(self):
        a = Node("A", "B", 3)
        nodes = {a}
        self.assertEqual(a, self.g.get_node_with_lowest_value(nodes))
        b = Node("B", "C", 2)
        nodes.add(b)
        self.assertEqual(b, self.g.get_node_with_lowest_value(nodes))
        c = Node("C", None, 0)
        d = Node("D", None, None)
        nodes.add(c)
        nodes.add(d)
        self.assertEqual(c, self.g.get_node_with_lowest_value(nodes))

    def test_get_path_from(self):
        self.g = Graph(["A", "B", "C", "D"])
        self.g.add_not_oriented_connections([["A", "B"], ["B", "C"], ["D", "C"]])
        self.assertEqual(7, len(self.g.get_path_from(Node("A"))))

    def test_add_connection_to_every_node(self):
        self.g.add_connection_to_every_node(self.g.nodes[0], 0, False)
        self.assertEqual(len(self.g.nodes) - 1, len(self.g.connections))

    def test_get_hamilton_path(self):
        self.g = Graph(["A", "B", "C", "D"])
        connections = [["A", "B", 10], ["A", "C", 3], ["A", "D", 2], ["B", "C", 1], ["B", "D", 5], ["C", "D", 7]]
        self.g.add_not_oriented_valued_connections(connections)
        self.assertEqual(7, len(self.g.get_hamilton_path()))

    def test_get_hamilton_path_nodes(self):
        self.g = Graph(["A", "B", "C", "D"])
        connections = [["A", "B", 10], ["A", "C", 3], ["A", "D", 2], ["B", "C", 1], ["B", "D", 5], ["C", "D", 7]]
        self.g.add_not_oriented_valued_connections(connections)
        self.assertEqual(4, len(self.g.get_hamilton_path_nodes()))
        self.assertIn(self.g.get_hamilton_path_nodes(), [[Node("B"), Node("C"), Node("A"), Node("D")],
                                                         [Node("A"), Node("D"), Node("C"), Node("B")]])
    def test_get_hamilton_path_nodes2(self):
        self.g = Graph(["A", "B", "C", "D"])
        connections = [["A", "B", 1], ["B", "C", 2], ["C", "D", 1], ["D", "A", 3], ["A", "C", 3], ["B", "D", 2]]
        self.g.add_not_oriented_valued_connections(connections)
        self.assertEqual(4, len(self.g.get_hamilton_path_nodes()))
        self.assertIn(self.g.get_hamilton_path_nodes(), [[Node("A"), Node("B"), Node("C"), Node("D")],
                                                         [Node("A"), Node("B"), Node("D"), Node("C")],
                                                         [Node("C"), Node("D"), Node("B"), Node("A")],
                                                         [Node("D"), Node("C"), Node("B"), Node("A")],
                                                         [Node("A"), Node("D"), Node("C"), Node("B")],
                                                         [Node("B"), Node("C"), Node("D"), Node("A")]])

    def test_get_hamilton_path_distance(self):
        self.g = Graph(["A", "B", "C", "D"])
        connections = [["A", "B", 10], ["A", "C", 3], ["A", "D", 2], ["B", "C", 1], ["B", "D", 5], ["C", "D", 7]]
        self.g.add_not_oriented_valued_connections(connections)
        self.assertTrue(14 > self.g.get_hamilton_path_distance())

    def test_get_three_node_combinations_without_repetition(self):
        self.assertEqual(20, len(self.g.get_three_node_combinations_without_repetition()))

    def test_get_three_nodes_with_most_unique_neigbors(self):
        self.g.add_not_oriented_connections([["A", "B"], ["B", "C"], ["D", "E"]])
        self.assertTrue(
            {Node("B"), Node("D"), Node("F")} == self.g.get_three_nodes_with_most_unique_neigbors()
            or {Node("B"), Node("E"), Node("F")} == self.g.get_three_nodes_with_most_unique_neigbors()
        )

    def test_nodes_as_str(self):
        self.assertEqual("A, B, C", self.g.nodes_as_str(['A', "B", "C"]))


if __name__ == '__main__':
    unittest.main()
