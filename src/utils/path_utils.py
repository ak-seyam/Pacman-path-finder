from typing import List
from models import Graph, Maze_map, Map_point, Map_el, Location



def multi_point_path(targets_dict):
    path = []
    for key in targets_dict:
        path += targets_dict[key][:-1]

    return path


def targets_to_nodes(maze_map, targets_id: List[int], start_node_id):
    ''' find the path betwean target nodes with a_star'''
    path_dict = {}
    targets_id.reverse()

    for i in range(1, len(targets_id)):
        start_node = maze_map.graph.nodes[targets_id[i-1]]
        end_node = maze_map.graph.nodes[targets_id[i]]
        path = a_star_one_target_path_only(start_node, end_node)
        path = [n.id for n in path]
        path.reverse()
        path_dict[targets_id[i]] = path

    return path_dict


def path_id_to_distance(maze_map,list_node_ids):
    list_nodes = [maze_map.graph.nodes[id_] for id_ in list_node_ids]
    return path_to_distance(list_nodes)


def path_to_distance(list_nodes):
    ''' get the distance to go through the list nodes path'''
    distance = 0
    for i in range(1, len(list_nodes)):
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
