import unittest
from Graph import Graph

class GraphTest(unittest.TestCase):

    def test_add_node(self):
        g = Graph(["A","B"])
        self.assertTrue(g.hasNode("A"))
        

if __name__ == '__main__':
    unittest.main()
