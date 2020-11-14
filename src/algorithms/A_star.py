from models.graph import Graph
from models.maze_map import Maze_map
from utils.graph_preprocessor import graph_algorithm


def a_star(maze_map: Maze_map, starting_node_id: int):
    current_node = maze_map.graph.get_node_by_id(starting_node_id)
    target_nodes = []
    for target in maze_map.traget:
        target_nodes.append(maze_map._get_node_by_location(target.location))

    moving_map_nodes = {}
    cost_map_nodes = {}
    # TODO sort targets
    list_heuristic = [(t.id, t.heuristics(current_node)) for t in target_nodes]

    n_targets = len(target_nodes)
    for _ in range(n_targets):
        target_node = min(
            target_nodes, key=lambda target: current_node.heuristics(target))
        moving_map_nodes[target_node], cost_map_nodes[target_node] = one_target(
            maze_map, maze_map.graph, current_node, target_node)
        current_node = target_node
        target_nodes.remove(target_node)

    moving_map = {}
    cost_map = {}
    for k in moving_map_nodes.keys():
        moving_map[k.id] = [n.id for n in moving_map_nodes[k] if n is not None]
        cost_map[k.id] = cost_map_nodes[k]

    return moving_map, cost_map


def one_target(maze_map, graph, start_node, end_node):

    cost_value = {start_node: start_node.heuristics(end_node)}
    visited_nodes = []
    current_node = start_node
    _res = {start_node: start_node}

    while current_node != end_node:
        connected_nodes = maze_map.connected_nodes(current_node)

        path = expan_to_path(maze_map, visited_nodes + [current_node])
        distance_to_current_node = path_to_distance(path)
        for node in connected_nodes:
            if node not in visited_nodes:
                distance = current_node.distance(
                    node) + distance_to_current_node
                # total_distance  =
                heuristics = current_node.heuristics(end_node)
                cost = distance + heuristics
                cost_value[node] = cost

        cost_value.pop(current_node, None)
        visited_nodes.append(current_node)

        current_node = min(cost_value.keys(), key=lambda k: cost_value[k])

    # add the target
    visited_nodes.append(current_node)
    path = expan_to_path(maze_map, visited_nodes)
    return path, path_to_distance(path)


def expan_to_path(maze_map, list_nodes):
    list_nodes = list_nodes[:]

    next_parent = None if len(list_nodes) == 1 else list_nodes[-1]
    path = [list_nodes[-1]]
    list_nodes.reverse()

    while next_parent is not None:
        next_index = list_nodes.index(next_parent)
        list_nodes = list_nodes[next_index:]
        next_parent = get_next_parent(
            maze_map, list_nodes, next_parent)
        if next_parent:
            path.append(next_parent)

    path.reverse()
    return path


def path_to_distance(list_nodes):
    distance = 0
    for i in range(1,len(list_nodes)):
        distance += list_nodes[i-1].distance(list_nodes[i])
    return distance


def get_next_parent(maze_map, list_nodes, node):
    for n in list_nodes:
        if n in maze_map.connected_nodes(node):
            return n
