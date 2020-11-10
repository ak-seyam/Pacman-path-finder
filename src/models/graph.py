from models.maze_items import Map_point

class Node(object):
    def __init__(self, id: int, map_point: Map_point = (-1, -1)):
        self.id = id
        self.edges = []
        self.map_point = map_point


class Edge(object):
    def __init__(self, id:int, node_from:Node, node_to:Node, distance=-1):
        self.id = id
        self.node_from = node_from
        self.node_to = node_to
        self.distance = distance


class Graph(object):
    def __init__(self, nodes=[], edges=[]):
        self.nodes = nodes
        self.edges = edges

    def insert_node(self, new_node_id, location: Map_point):
        new_node = Node(new_node_id, location)
        self.nodes.append(new_node)
    

    def insert_edge(self, new_edge_id, node_from_id, node_to_id, distance=-1):
        from_found = None
        to_found = None
        for node in self.nodes:
            if node_from_id == node.id:
                from_found = node
            if node_to_id == node.id:
                to_found = node
        if from_found == None:
            from_found = Node(node_from_id)
            self.nodes.append(from_found)
        if to_found == None:
            to_found = Node(node_to_id)
            self.nodes.append(to_found)
        new_edge = Edge(new_edge_id, from_found, to_found, distance)
        from_found.edges.append(new_edge)
        to_found.edges.append(new_edge)
        self.edges.append(new_edge)
    def get_node_by_id(self,node_id):
        for node in self.nodes:
            if node.id == node_id:
                return node

    def get_edge_by_id(self,edge_id):
        for edge in self.edges:
            if edge.id == edge_id:
                return edge

    def get_edge_list(self):
        """Don't return a list of edge objects!
        Return a list of triples that looks like this:
        (Edge id, From Node id, To Node id)"""
        return [(e.id, e.node_from.id, e.node_to.id) for e in self.edges]
        

    def get_adjacency_list(self):
        """Don't return any Node or Edge objects!
        You'll return a list of lists.
        The indecies of the outer list represent
        "from" nodes.
        Each section in the list will store a list
        of tuples that looks like this:
        (To Node, Edge id)"""
        
        adjc_list = [None]*(len(self.nodes)+1)
        for node in self.nodes:
            row = []
            for e in node.edges:
                if e.node_to != node:
                    row.append((e.node_to.id, e.id))
            if row:
                adjc_list[node.id] = row
            
        return adjc_list

    def get_adjacency_matrix(self):
        """Return a matrix, or 2D list.
        Row numbers represent from nodes,
        column numbers represent to nodes.
        Store the edge ids in each spot,
        and a 0 if no edge exists."""
        n_nodes = len(self.nodes)+1
        adj_mat = [[0]*n_nodes for i in range(n_nodes)]
        for e in self.edges:
            adj_mat[e.node_from.id][e.node_to.id] = e.id
        
        return adj_mat

class GraphStructureError(Exception):
    """
        An exception raised for graphs with non correct structure for example
        graphs with nodes but no edges
    """
    pass

if __name__ == "__main__":
    # test
    graph = Graph()
    graph.insert_edge(100, 1, 2)
    graph.insert_edge(101, 1, 3)
    graph.insert_edge(102, 1, 4)
    graph.insert_edge(103, 3, 4)
    # Should be [(100, 1, 2), (101, 1, 3), (102, 1, 4), (103, 3, 4)]
    print (graph.get_edge_list())
    # Should be [None, [(2, 100), (3, 101), (4, 102)], None, [(4, 103)], None]
    print (graph.get_adjacency_list())
    # Should be [[0, 0, 0, 0, 0], [0, 0, 100, 101, 102], [0, 0, 0, 0, 0], [0, 0, 0, 0, 103], [0, 0, 0, 0, 0]]
    print (graph.get_adjacency_matrix())
