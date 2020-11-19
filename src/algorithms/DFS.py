from models.graph import Graph
from utils.graph_preprocessor import graph_algorithm
from typing import Callable

# TODO: try to make a generic BFS
# @graph_algorithm()
# def DFS(graph: Graph, starting_node_id):
    # """ Do a DFS over a graph """
    # target_node_ids = [node.id for node in graph.nodes if node.is_target()]
    # adjacency_dict = graph.get_adjacency_dict()
    # return lazyDFS_many(starting_node_id, target_node_ids, adjacency_dict)


# def lazyDFS_many(starting_node_id, target_node_ids, adjacency_dict):
#     moving_map = {}
#     while target_node_ids:
#         target_id, visited_nodes = find_next_target(
#             starting_node_id, target_node_ids, adjacency_dict)
#         # start at it next time and remove from targets
#         starting_node_id = target_id
#         target_node_ids.remove(target_id)
#         # add node to dict
#         moving_map[target_id] = visited_nodes

#     return moving_map

# def uniformed_serch(starting_node_id, target_node_ids, adjacency_dict):
#     visited_nodes = list()  # i need to keep track of the order
#     nodes_stack = [starting_node_id]

#     while len(nodes_stack):
#         node_id = nodes_stack.pop(-1)  # remove the last element, LIFO

#         if node_id not in visited_nodes:
#             visited_nodes.append(node_id)
#             if node_id in target_node_ids:
#                 return node_id, visited_nodes
#             connections = adjacency_dict.get(node_id)
#             if connections:
#                 for connection in connections:
#                     # add the to index to nodes stack
#                     nodes_stack.append(connection[0])


def dfs_single_target(starting_node_id, target_node_id, adjacency_dict):
    traget_locator = lambda node_id: node_id == target_node_id
    return dfs_generic(starting_node_id, traget_locator, adjacency_dict)


def dfs_generic(starting_node_id, traget_locator: Callable, adjacency_dict):
    visited_nodes = list()  # i need to keep track of the order
    nodes_stack = [starting_node_id]

    while len(nodes_stack):
        node_id = nodes_stack.pop(-1)  # remove the last element, LIFO

        if node_id not in visited_nodes:
            visited_nodes.append(node_id)
            # find the target
            if traget_locator(node_id):
                return node_id, visited_nodes
            
            connections = adjacency_dict.get(node_id)
            if connections:
                for connection in connections:
                    # add the to index to nodes stack
                    nodes_stack.append(connection[0])
    return visited_nodes