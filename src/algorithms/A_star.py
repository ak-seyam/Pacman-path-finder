from models.graph import Graph
from models.maze_map import Maze_map
from models.maze_items import Map_point
from utils.graph_preprocessor import graph_algorithm
from typing import List


def a_star(maze_map: Maze_map, starting_node_id: int):
    current_node = maze_map.graph.get_node_by_id(starting_node_id)
    target_nodes = []
    for target in maze_map.traget:
        target_nodes.append(maze_map._get_node_by_location(target.location))

    moving_map_nodes = {}
    cost_map_nodes = {}
    # TODO sort targets
    # list_heuristic = [(t.id, t.heuristics(current_node)) for t in target_nodes]

    n_targets = len(target_nodes)
    for _ in range(n_targets):
        target_node = min(
            target_nodes, key=lambda target: current_node.heuristics(target))
        moving_map_nodes[target_node], cost_map_nodes[target_node] = a_star_one_target(current_node, target_node)
        current_node = target_node
        target_nodes.remove(target_node)

    moving_map = {}
    cost_map = {}
    for k in moving_map_nodes.keys():
        moving_map[k.id] = [n.id for n in moving_map_nodes[k] if n is not None]
        cost_map[k.id] = cost_map_nodes[k]

    return moving_map, cost_map


def expand_id_generator():
    expand_id = 0
    while True:
        yield expand_id
        expand_id += 1


def a_star_one_target(start_node, end_node):
    exp_gen = expand_id_generator()
    
    node_parent_distance = {start_node: (None,0)}  # node : (parent,distance)
    distance_to_current_node = 0
    cost_value = {start_node: start_node.heuristics(end_node)} # (node):cost

    visited_nodes = []
    current_node = start_node
    _res = {start_node: start_node}

    while current_node != end_node:
        connected_nodes = current_node.connected_nodes()

        # path = expan_to_path(visited_nodes + [current_node])
        # distance_to_current_node = path_to_distance(path)
        parent , parent_distance = node_parent_distance[current_node]
        if parent:
            distance_to_current_node = parent_distance + parent.distance(current_node)
        
        for node in connected_nodes: # node is the expanded nodes
            if node not in visited_nodes:
                distance = current_node.distance(
                    node) + distance_to_current_node
                heuristics = current_node.heuristics(end_node)
                cost = distance + heuristics
                # if value in cost smaller don't add
                old_cost = cost_value.get(node,None)

                if old_cost:
                    if cost < old_cost:
                        cost_value[node] = cost
                        node_parent_distance[node] = (current_node,distance_to_current_node)
                else:
                    cost_value[node] = cost
                    node_parent_distance[node] = (current_node,distance_to_current_node)


        cost_value.pop(current_node, None)
        visited_nodes.append(current_node)

        current_node = min(cost_value.keys(), key=lambda k: cost_value[k])

    # add the target
    visited_nodes.append(current_node)
    # path = expan_to_path(visited_nodes)
    path = parent_list_distance_to_path(node_parent_distance, end_node)
    return path, path_to_distance(path)


def parent_list_to_path(node_parent,node):
    path = [node]
    while node:
        parent = node_parent.get(node,(None,None))
        if parent:
            path.append(parent)
        node = parent
    
    return path

def parent_list_distance_to_path(node_parent,node):
    for k in node_parent.keys():
        parent_node ,distance= node_parent[k]
        node_parent[k] = parent_node

    return parent_list_to_path(node_parent, node)





def path_to_distance(list_nodes):
    ''' get the distance to go through the list nodes path'''
    distance = 0
    for i in range(1, len(list_nodes)):
        if i ==31:
            x=1
        distance += list_nodes[i-1].distance(list_nodes[i])
    return distance

def path_to_points(list_nodes) -> List[Map_point]:
    ''' get detaialed route as map_points for the path'''
    route = []
    for i in range(1, len(list_nodes)):
        last_node = list_nodes[i-1]
        current_node = list_nodes[i]
        route += last_node.connected_nodes_route()[current_node.id]
    return route
