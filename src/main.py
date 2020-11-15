from models import Graph, Maze_map, Map_point, Map_el, Location
from algorithms.BFS import BFS
# from algorithms.DFS import dfs_single_target
from algorithms.GFS import GFS
from algorithms.GFS_Solver import GFS_Solver
from algorithms.BFS_sovler import BFS_Solver
from utils.informed_multi_target_solver import informed_multi_target_solver
from algorithms.A_star import a_star


mazes = [
    'bigDots.txt', 'bigMaze.txt', 'mediumMaze.txt', 'mediumSearch.txt', 'openMaze.txt', 'smallSearch.txt', 'tinySearch.txt']


maze_map = Maze_map(f'Maze/{mazes[0]}')

starting_point = maze_map.get_node_by_map_point(maze_map.player).id
print(maze_map)

# GFS solver
# graph = maze_map.graph
# sol = GFS_Solver(graph, starting_point)
# informed_multi_target_solver(
#     GFS, graph, starting_point, maze_map, sol.solve, sol.steps_counter)
# print('result path', sol.get_path())
# print('result expansion', sol.expansion)
# print('#steps: ', sol.steps)
# print('total cost', sol.res_path_cost())


# BFS solution
# sol = BFS_Solver(starting_point, maze_map.graph, maze_map)
# BFS(maze_map.graph, starting_point, sol.solver, sol.steps_counter)
# print('result is: ',sol._res)
# print('result is: ',sol.get_result())
# print('expansion is: ',sol.expansion)
# print('#steps: ',sol.steps)
# print('total cost', sol.res_path_cost())


# test map convertion
# print(maze_map)
# for i in maze_map.graph.get_adjacency_list():
#     print(i)
# for i in maze_map.node_map():
#     print(i)

# Solver code

def solve_a_star(maze_map):
    player_point = maze_map.player
    start_node_id = maze_map._get_node_by_location(player_point.location).id
    moving_map = a_star(maze_map, start_node_id)
    for k in moving_map.keys():
        print(k, moving_map[k])


def solve_dfs(maze_map):
    player_point = maze_map.player
    start_node_id = maze_map._get_node_by_location(player_point.location).id

    moving_map = DFS(maze_map.graph, start_node_id)
    for k in moving_map.keys():
        print(k, moving_map[k])

# DFS solution
# for map_ in mazes:
#     print(map_)
#     # map_ = mazes[-1]
#     maze_map = Maze_map(f'Maze/{map_}')
#     print(maze_map)
#     solve_dfs(maze_map)


# a_star solution
# for map_ in mazes:
# # map_ = mazes[2]
# # map_ = mazes[-1]
#     maze_map = Maze_map(f'Maze/{map_}')
#     print(maze_map)
#     print(solve_a_star(maze_map))
