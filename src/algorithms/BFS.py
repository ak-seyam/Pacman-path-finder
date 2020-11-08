from models.graph import Graph


def BFS(graph: Graph, starting_node, callback=print):
    """
    Do a BFS over a graph
    """
    if len(graph.nodes) == 0:
        return
    elif len(graph.edges) == 0:  # nodes are empty but are not
        callable(starting_node)

