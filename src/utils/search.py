import enum
from models.maze_map import Maze_map
from algorithms.GFS_Solver import GFS_Solver
from algorithms.BFS_sovler import BFS_Solver
from utils.informed_multi_target_solver import informed_multi_target_solver
from algorithms.GFS import GFS
from algorithms.BFS import BFS
from algorithms.multi_target import a_star_multi_target

class search_type(enum.Enum):
    DFS = 0
    BFS = 1
    GFS = 2
    A_Star = 3

def search(algorithm:search_type, maze_map:Maze_map, log:bool= True):
    graph = maze_map.graph
    starting_point = maze_map.get_node_by_map_point(maze_map.player).id

    if algorithm == search_type.DFS:
        player_point = maze_map.player
        start_node_id = maze_map._get_node_by_location(player_point.location).id

        moving_map = DFS(maze_map.graph, start_node_id)
        if log:
            for k in moving_map.keys():
                print(k, moving_map[k])
        return moving_map

    elif algorithm == search_type.A_Star:
        # TODO ask abdo about log
        return a_star_multi_target(maze_map, maze_map.player.node_id)

    elif algorithm == search_type.BFS:
        sol = BFS_Solver(starting_point, maze_map.graph, maze_map)
        BFS(maze_map.graph, starting_point, sol.solver, sol.steps_counter)

        if log :
            print('result is: ',sol.get_result())
            print('expansion is: ',sol.expansion)
            print('#hits: ',sol.num_hits)
            print('total cost', sol.res_path_cost())
        return sol.get_result()

    elif algorithm == search_type.GFS:
        sol = GFS_Solver(graph, starting_point)
        informed_multi_target_solver(
            GFS, graph, starting_point, maze_map, sol.solve, sol.steps_counter)

        if log :
            print('result path', sol.get_path())
            print('result expansion', sol.expansion)
            print('#hits: ', sol.num_hits)
            print('total cost', sol.res_path_cost())
        return sol.get_path()

    else :
        raise ValueError("Invalid Algorithm")