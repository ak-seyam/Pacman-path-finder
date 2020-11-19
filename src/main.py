from models import Graph, Maze_map, Map_point, Map_el, Location
from algorithms.BFS import BFS
from algorithms.DFS import dfs_single_target
from algorithms.GFS import GFS
from algorithms.GFS_Solver import GFS_Solver
from algorithms.BFS_sovler import BFS_Solver
from utils.informed_multi_target_solver import informed_multi_target_solver
from algorithms.A_star import a_star, path_to_distance,a_star_one_target


mazes = [
    'bigDots.txt', 'bigMaze.txt', 'mediumMaze.txt', 'mediumSearch.txt', 'openMaze.txt', 'smallSearch.txt', 'tinySearch.txt']


# maze_map = Maze_map(f'Maze/{mazes[4]}')

# starting_point = maze_map.get_node_by_map_point(maze_map.player).id

#GFS solver
# sol = GFS_Solver(starting_point)
# informed_multi_target_solver(GFS,maze_map.graph,starting_point,maze_map, sol.solve, sol.steps_counter)
# print('result path',sol.get_path())
# print('result expansion',sol.expansion)
# print('#steps: ',sol.steps)


# BFS solution
# sol = BFS_Solver(starting_point, maze_map.graph, maze_map)
# BFS(maze_map.graph, starting_point, sol.solver, sol.steps_counter)
# print('result is: ',sol.get_result())
# print('expansion is: ',sol.expansion)
# print('#steps: ',sol.steps)

# print(maze_map)


# test map convertion
# print(maze_map)
# for i in maze_map.graph.get_adjacency_list():
#     print(i)
# for i in maze_map.node_map():
#     print(i)

# Solver code



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
# map_ = mazes[2]
# map_ = mazes[0]
    # maze_map = Maze_map(f'Maze/{map_}')
    # print(maze_map)
    # solve_a_star(maze_map)

# part 1
# DFS
part_1_mazes = [
    "bigMaze.txt",
    "mediumMaze.txt",
    "openMaze.txt"
]

# a*
# for maze_name in part_1_mazes:
#     maze_map = Maze_map(f'Maze/{maze_name}')
#     start_node = maze_map.get_node_by_map_point(maze_map.player)
#     target_node = maze_map.get_node_by_map_point(maze_map.traget[0])
#     adjc_dict = maze_map.graph.get_adjacency_dict()
#     # path = dfs_single_target(start_node_id, target_node_id, adjc_dict)
#     path, cost = a_star_one_target(start_node, target_node)
#     with open(f'sol/a_star/{maze_name}', 'w') as sol_file:
#         # sol_file.write(str(maze_map))
#         sol_file.write(str([n.id for n in path])+'\n')
#         sol_file.write('cost = ' + str(cost))

