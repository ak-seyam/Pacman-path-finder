from models.graph import Graph
from utils.graph_preprocessor import graph_algorithm


@graph_algorithm()
def GFS(graph: Graph, starting_node_id, maze_map, callback=lambda node: print(f"Node Id = {node.id}")):
    pass    

def _GFS(graph: Graph, starting_node_id, target, callback=lambda node: print(f"Node Id = {node.id}")):
    visited_nodes = set()
    adjacency_dict = graph.get_adjacency_dict()
    path = [starting_node_id]
    next = starting_node_id
    while next != target :
        callable(graph[next])
        next = _get_closet_child(graph, next, adjacency_dict[next])
        path.append(next)

    return {starting_node_id : path}
    

def _get_closet_child(graph,parent:int,children:list) -> int:
    # get the heuristic distance for all children
    # return minimum 
    parent_node = graph.nodes[parent]
    shortest_distance = float('inf')
    closest = -1
    for child in children :
        distance = parent_node.heuristic(
            graph.nodes[child]
        )
        if distance < shortest_distance :
            shortest_distance = distance
            closest = child
    return closest