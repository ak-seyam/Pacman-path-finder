from models.graph import Graph
from utils.graph_preprocessor import graph_algorithm
from algorithms.BFS import lazyBFS

_adjacency_dict = {}

@graph_algorithm()
def GFS(graph: Graph, starting_node_id, target_id, callback=lambda node: print(f"Node Id = {node.id}")):
    _adjacency_dict = graph.get_adjacency_dict()
    path = [starting_node_id]
    next = starting_node_id
    while next != target_id :
        callback(graph[next])
        children = [x[0] for x in _adjacency_dict[next]]
        next = get_the_closet_to_target_child(graph,children,target_id)
        
def get_the_closet_to_target_child(graph, children_ids, target_id):
    children_nodes = [graph.nodes[id] for id in children_ids]
    minimum_child = children_ids[0]
    minimum_child_distance = children_nodes[0].heuristic(graph[target_id])
    for index in range(1,len(children_ids)) :
        distance = children_nodes[index].heuristic(graph[target_id]) 
        if  distance < minimum_child_distance :
            minimum_child = children_ids[index]
            minimum_child_distance = distance
            
    return minimum_child

# get hubristic for all children