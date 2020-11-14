from utils.closet_target import get_closest_target, clear_visited_targets
from models.graph import Graph
from models.maze_map import Maze_map

def multi_target_solver(algorithm, graph: Graph, \
                        starting_node_id, \
                        maze_map: Maze_map, \
                        callback, \
                        steps_counter=None):
    targets = maze_map.traget
    prev_target_id = starting_node_id

    for _ in range(len(targets)):
        target_id = get_closest_target(prev_target_id, maze_map)
        if steps_counter != None :
            algorithm(graph, prev_target_id, target_id, callback, steps_counter)
        else :
            algorithm(graph, prev_target_id, target_id, callback)
        prev_target_id = target_id

    clear_visited_targets()
