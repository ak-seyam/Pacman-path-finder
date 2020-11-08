from models.graph import Graph
from utils.graph_preprocessor import graph_algorithm


@graph_algorithm()
def BFS(graph: Graph, starting_node_index, callback=lambda node: print(f"Node Id = {node.id}")):
    """
    Do a BFS over a graph

    NOTE: callback is a function that gets called after each node being visited
    NOTE: callback is expected to take a Node object only as an argument
    """
    visited_nodes = set()
    adjacency_list = graph.get_adjacency_list()
    nodes_queue = [starting_node_index]
    while len(nodes_queue):
        node = nodes_queue.pop(0)  # remove the first element, FIFO
        if node not in visited_nodes:
            visited_nodes.add(node)
            callback(graph.nodes[node])
            connections = adjacency_list.get(node)
            if connections:
                for connection in connections:
                    # add the to index to nodes queue
                    nodes_queue.append(connection[0])
