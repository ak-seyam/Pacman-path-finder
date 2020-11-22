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


class search():
    def __init__(self, algorithm: int, maze_map: Maze_map):
        self.algorithm = algorithm
        self.maze_map = maze_map
        self.graph = maze_map.graph
        self.starting_point = maze_map.get_node_by_map_point(
            maze_map.player).id

    def get_path(self, log: bool = False):

        if self.algorithm == search_type.DFS:
            moving_map = DFS(self.maze_map.graph, self.start_node_id)
            if log:
                for k in moving_map.keys():
                    print(k, moving_map[k])
            return moving_map

        elif self.algorithm == search_type.A_Star:
            return a_star_multi_target(self.maze_map, self.maze_map.player.node_id)

        elif self.algorithm == search_type.BFS:
            sol = BFS_Solver(self.starting_point,
                             self.maze_map.graph, self.maze_map)
            BFS(self.maze_map.graph, self.starting_point,
                sol.solver, sol.steps_counter)

            if log:
                print('result is: ', sol.get_result())
                print('expansion is: ', sol.expansion)
                print('#hits: ', sol.num_hits)
                print('total cost', sol.res_path_cost())
            return sol.get_result()

        elif self.algorithm == search_type.GFS:
            sol = GFS_Solver(self.graph, self.starting_point)
            informed_multi_target_solver(
                GFS, self.graph, self.starting_point, self.maze_map, sol.solve, sol.steps_counter)

            if log:
                print('result path', sol.get_path())
                print('result expansion', sol.expansion)
                print('#hits: ', sol.num_hits)
                print('total cost', sol.res_path_cost())
            return sol.get_path()
