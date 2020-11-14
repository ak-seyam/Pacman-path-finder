from models.maze_map import Maze_map
_visited_targets = list()


def get_closest_target(current_position_id: int, maze_map: Maze_map) -> int:
    """
        Get ID of the closest node to the current node position id in the map
        Or return None if all nodes are visited
    """
    if len(_visited_targets) == len(maze_map.traget):
        return None

    targets = [maze_map.get_node_by_map_point(
        target) for target in maze_map.traget]
    targets = filter(lambda target: target.id != current_position_id, targets)
    closet_target = None
    minimum_distance = float('inf')
    current_node = maze_map.graph.nodes[current_position_id]
    for target in targets:
        distance = target.heuristics(current_node)
        if distance < minimum_distance and target.id not in _visited_targets:
            closet_target = target.id
            minimum_distance = distance
    _visited_targets.append(closet_target)
    return closet_target


def clear_visited_targets():
    """
        Cleaning the visited targest for future useage, use it with caution
    """
    _visited_targets = []
