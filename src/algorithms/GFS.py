from models.graph import Graph
from utils.graph_preprocessor import graph_algorithm
from algorithms.BFS import lazyBFS
from models.maze_map import Maze_map
from utils.closet_target import get_closest_target, clear_visited_targets

_adjacency_dict = {}

# @graph_algorithm()
# def GFS(graph: Graph, starting_node_id, maze_map: Maze_map ,callback, steps_counter):
#     targets = maze_map.traget
#     prev_target_id = starting_node_id
#     for _ in range(len(targets)):
#         target_id = get_closest_target(prev_target_id, maze_map)
#         _GFS(graph,prev_target_id,target_id, callback, steps_counter)
#         prev_target_id=target_id
#     clear_visited_targets()    
@graph_algorithm()
def GFS(graph: Graph, starting_node_id, target_id, callback, steps_counter):
    _adjacency_dict = graph.get_adjacency_dict()
    visited_nodes = list()
    next = starting_node_id
    backtrack_index = -1
    while next != target_id :
        steps_counter() # for each node traversal count the steps
        children = list()
        if next!=None : # if it's not stuck
            callback(graph.nodes[next])
            visited_nodes.append(next)
            children = [x[0] for x in _adjacency_dict[next]]
        else : # if it is stuck 
            backtrack_index -= 1 # get the children of the previous node aka backtrack
            children = [x[0] for x in _adjacency_dict[visited_nodes[backtrack_index]]] # get the children of the previously visited nodes
        next = get_the_closet_to_target_child(graph,children,target_id, visited_nodes)
    callback(graph.nodes[target_id])
        
def get_the_closet_to_target_child(graph, children_ids, target_id, exce):
    children_nodes = [graph.nodes[id] for id in children_ids]
    minimum_child = None
    minimum_child_distance = float('inf')
    for index in range(len(children_ids)) :
        distance = children_nodes[index].heuristics(graph.nodes[target_id]) 
        if  distance < minimum_child_distance and children_ids[index] not in exce:
            minimum_child = children_ids[index]
            minimum_child_distance = distance
            
    return minimum_child

# get hubristic for all children
