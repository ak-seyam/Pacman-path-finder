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
        self.bfs_sol = BFS_Solver(
            self.starting_point, self.graph, self.maze_map)
        self.gfs_sol = GFS_Solver(
            self.graph, self.starting_point)
        # for gfs and bfs we shall solve them to use the

    def get_path(self, log: bool = False):
        """
            This function return the result path.
            
            NOTE [1]: In case of BFS and GFS if log is false this function will run 
            faster because it will skip calculating the expanded path to be cached
            later and will lazy load it if needed

            Parameters:
            log: bool = False:
                Wither to log or not see [1]
        """

        if self.algorithm == search_type.DFS:
            # NOTE abdo should check this error
            moving_map = DFS(self.maze_map.graph, self.starting_point)
            if log:
                for k in moving_map.keys():
                    print(k, moving_map[k])
            return moving_map

        elif self.algorithm == search_type.A_Star:
            return a_star_multi_target(self.maze_map, self.maze_map.player.node_id)

        elif self.algorithm == search_type.BFS:
            BFS(self.maze_map.graph, self.starting_point,
                self.bfs_sol.solver, self.bfs_sol.steps_counter)

            res = self.bfs_sol.get_result()
            if log:
                print('result is: ', res)
                print('expansion is: ', self.bfs_sol.expansion)
                print('#hits: ', self.bfs_sol.num_hits)
                print('total cost', self.bfs_sol.res_path_cost())
            return res

        elif self.algorithm == search_type.GFS:
            informed_multi_target_solver(
                GFS, self.graph, self.starting_point, self.maze_map,
                self.gfs_sol.solve, self.gfs_sol.steps_counter)

            res = self.gfs_sol.get_path()
            if log:
                print('result path', res)
                print('result expansion', self.gfs_sol.expansion)
                print('#hits: ', self.gfs_sol.num_hits)
                print('total cost', self.gfs_sol.res_path_cost())
            return res

    def get_cost(self):
        if self.algorithm == search_type.A_Star:
            # NOTE abdo should add A_Star cost here
            pass
        elif self.algorithm == search_type.DFS:
            # NOTE abdo should add DFS cost here
            pass
        elif self.algorithm == search_type.BFS:
            # TODO cache sol results for BFS and GFS
            return self.bfs_sol.res_path_cost()
        elif self.algorithm == search_type.GFS:
            # TODO cache sol results for BFS and GFS
            return self.gfs_sol.res_path_cost()
        else:
            raise ValueError("Invalid algorithm")

    def get_expansion(self):
        if self.algorithm == search_type.A_Star:
            # NOTE abdo should add A_Star expansion here
            pass
        elif self.algorithm == search_type.DFS:
            # NOTE abdo should add DFS expansion here
            pass
        elif self.algorithm == search_type.BFS:
            return self.bfs_sol.expansion
        elif self.algorithm == search_type.GFS:
            return self.gfs_sol.expansion

    def get_number_of_expanded_nodes(self):
        if self.algorithm == search_type.A_Star:
            # NOTE abdo should add A_Star #expansion here
            pass
        elif self.algorithm == search_type.DFS:
            # NOTE abdo should add DFS #expansion here
            pass
        elif self.algorithm == search_type.BFS:
            # TODO cache sol results for BFS and GFS
            return self.bfs_sol.num_hits
        elif self.algorithm == search_type.GFS:
            # TODO cache sol results for BFS and GFS
            return self.gfs_sol.num_hits
