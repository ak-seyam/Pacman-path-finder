import unittest
import doctest


from ..graph import Graph
# class TestEdges(unittest.TestCase):
# def test_edge_other_node

# def load_tests(loader, tests, ignore):
#     tests.addTests(doctest.DocTestSuite(my_module_with_doctests))
#     return tests


class TestGraph(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        cls.graph = Graph()
        cls.graph.insert_edge(100, 1, 2)
        cls.graph.insert_edge(101, 1, 3)
        cls.graph.insert_edge(102, 1, 4)
        cls.graph.insert_edge(103, 3, 4)
        
    # def tearDown(self):
    #     del self.graph

    def test_edge_list(self):
        self.assertEqual(self.graph.get_edge_list(), [
                         (100, 1, 2), (101, 1, 3), (102, 1, 4), (103, 3, 4)])

    def test_adjacency_list(self):
        self.assertEqual(self.graph.get_adjacency_list(), [
                         None, [(2, 100), (3, 101), (4, 102)], None, [(4, 103)], None])

    def test_adjacency_matrix(self):
        self.assertEqual(self.graph.get_adjacency_matrix(), [[0, 0, 0, 0, 0], [0, 0, 100, 101, 102], [
            0, 0, 0, 0, 0], [0, 0, 0, 0, 103], [0, 0, 0, 0, 0]])
