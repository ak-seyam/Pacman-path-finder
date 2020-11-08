from models.graph import Graph
from utils.graph_preprocessor import graph_algorithm


@graph_algorithm()
def BFS(graph: Graph, starting_node_index, callback=print):
    """
    Do a BFS over a graph

    NOTE: callback is a function that gets called after each node being visited
    NOTE: callback is expected to take a Node object only as an argument
    """
    visited_nodes = set()
    adjacency_list = graph.get_adjacency_list()
    nodes_queue = [starting_node_index]
    for node in nodes_queue:
        if node not in visited_nodes:
            visited_nodes.add(node)
            nodes_queue.pop(0) # remove the first element, FIFO
            callback(graph.nodes[node])
            for connection in adjacency_list[node]:
                # add the to index to nodes queue
                nodes_queue.append(connection[0])
