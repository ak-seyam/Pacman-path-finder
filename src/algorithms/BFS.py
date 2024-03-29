from models.graph import Graph
from utils.graph_preprocessor import graph_algorithm


# TODO: try to make a generic BFS
@graph_algorithm()
def BFS(graph: Graph, starting_node_id, callback, steps_counter):
    """
    Do a BFS over a graph
    NOTE: callback is a function that gets called after each node being visited
    NOTE: callback is expected to take a Node object only as an argument
    """
    visited_nodes = set()
    adjacency_dict = graph.get_adjacency_dict()
    nodes_queue = [starting_node_id]
    while len(nodes_queue):
        node = nodes_queue.pop(0)  # remove the first element, FIFO
        if node not in visited_nodes:
            visited_nodes.add(node)
            connections = adjacency_dict.get(node)
            nodes_list = [node]
            nodes_list.extend(connections)
            callback(nodes_list)
            steps_counter()
            if connections:
                for connection in connections:
                    # add the to index to nodes queue
                    nodes_queue.append(connection[0])


def lazyBFS(starting_node_id, get_adjacent_nodes_ids,
            callback=None):
    """
        Do BFS but with lazy adjacency list loading, suitable for the unusual 
        adjacency list mechanism like the maze-graph converter or getting the
        adjacent list from an external source, for example getting them online
        TODO add target nodes id that BFS stop when reach them
    """
    visited_nodes = set()
    nodes_queue = [starting_node_id]
    while len(nodes_queue):
        node = nodes_queue.pop(0)
        if node not in visited_nodes:
            visited_nodes.add(node)
            if callback:
                callback(node)
            adjacent_nodes = get_adjacent_nodes_ids(node)
            if adjacent_nodes:
                nodes_queue.extend(adjacent_nodes)
