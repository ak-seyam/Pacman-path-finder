from models.maze_map import Maze_map
def get_closest_target(current_position_id: int, maze_map:Maze_map) -> int:
    """
        Get ID of the closest node to the current node position id in the map
    """
    targets = [maze_map.get_node_by_map_point(target) for target in maze_map.traget]
    targets = filter(lambda target: target.id != current_position_id, targets)
    closet_target = None
    minimum_distance = float('inf')
    current_node = maze_map.graph.nodes[current_position_id]
    for target in targets :
        distance = target.heuristics(current_node)
        if distance < minimum_distance :
            closet_target = target.id
            minimum_distance = distance
    return closet_target