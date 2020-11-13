from models.graph import Graph
from utils.graph_preprocessor import graph_algorithm
from algorithms.BFS import lazyBFS
from models.maze_map import Maze_map

_adjacency_dict = {}

@graph_algorithm()
def GFS(graph: Graph, starting_node_id, maze_map: Maze_map ,callback=lambda node: print(f"Node Id = {node.id}")):
    targets = maze_map.traget
    for target in targets:
        pass

def _GFS(graph: Graph, starting_node_id, target_id, callback=lambda node: print(f"Node Id = {node.id}")):
    _adjacency_dict = graph.get_adjacency_dict()
    visited_nodes = set()
    next = starting_node_id
    while next != target_id :
        callback(graph[next])
        children = [x[0] for x in _adjacency_dict[next]]
        next = get_the_closet_to_target_child(graph,children,target_id, visited_nodes)
        visited_nodes.add(next)

        
def get_the_closet_to_target_child(graph, children_ids, target_id, exce):
    children_nodes = [graph.nodes[id] for id in children_ids]
    minimum_child = children_ids[0]
    minimum_child_distance = children_nodes[0].heuristic(graph[target_id])
    for index in range(1,len(children_ids)) :
        distance = children_nodes[index].heuristic(graph[target_id]) 
        if  distance < minimum_child_distance and children_ids[index] not in exce:
            minimum_child = children_ids[index]
            minimum_child_distance = distance
            
    return minimum_child

# get hubristic for all children
