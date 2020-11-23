from models import Graph, Maze_map, Map_point, Map_el, Location
from algorithms.BFS import BFS
from algorithms.DFS import dfs_single_target
from algorithms.GFS import GFS
from algorithms.GFS_Solver import GFS_Solver
from algorithms.BFS_sovler import BFS_Solver
from utils.informed_multi_target_solver import informed_multi_target_solver
from utils.prepare_targets import prepare_targets
# from algorithms.A_star import a_star, path_to_distance, a_star_one_target, path_to_points
from utils.search import search_type, search


mazes = [
    'bigDots.txt', 'bigMaze.txt', 'mediumMaze.txt', 'mediumSearch.txt', 'openMaze.txt', 'smallSearch.txt', 'tinySearch.txt']


maze_map = Maze_map(f'Maze/{mazes[-1]}')

# NOTE testing common search logic
s = search(search_type.GFS, maze_map)

print(s.get_path())
print(s.get_cost())
print(s.get_expansion())
print(s.get_number_of_expanded_nodes())

# starting_point = maze_map.get_node_by_map_point(maze_map.player).id
# print(maze_map)

# # GFS solver
# graph = maze_map.graph
# sol = GFS_Solver(graph, starting_point)
# informed_multi_target_solver(
#     GFS, graph, starting_point, maze_map, sol.solve, sol.steps_counter)
# print('result path', sol.get_path())
# print('result expansion', sol.expansion)
# print('#hits: ', sol.num_hits)
# print('total cost', sol.res_path_cost())

# print(prepare_targets(maze_map, maze_map.player.node_id))
# print('------------------------------')

# BFS solution 
# sol = BFS_Solver(starting_point, maze_map.graph, maze_map)
# BFS(maze_map.graph, starting_point, sol.solver, sol.steps_counter)
# print('result is: ',sol.get_result())
# print('expansion is: ',sol.expansion)
# print('#hits: ',sol.num_hits)
# print('total cost', sol.res_path_cost())


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


# for maze_name in part_1_mazes:
#     maze_map = Maze_map(f'Maze/{maze_name}')
#     start_node = maze_map.get_node_by_map_point(maze_map.player)
#     target_node = maze_map.get_node_by_map_point(maze_map.traget[0])
#     adjc_dict = maze_map.graph.get_adjacency_dict()
    

    #a*
    # path, cost = a_star_one_target(start_node, target_node)
    # route = path_to_points(path)
    # with open(f'sol/a_star/{maze_name}', 'w') as sol_file:
    #     # sol_file.write(str(maze_map))
    #     sol_file.write(str([n.id for n in path])+'\n')
    #     sol_file.write('cost = ' + str(cost)+ '\n')
    #     sol_file.write('route = ' + str(route))

    # dfs
    # path_ids = dfs_single_target(start_node.id, target_node.id, adjc_dict)
    # # print(path_ids[path_ids[0]])
    # path = [maze_map.graph.nodes[id_] for id_ in path_ids]
    # cost  = path_to_distance(path)
    # route = path_to_points(path)
    # with open(f'sol/dfs/{maze_name}', 'w') as sol_file:
    #     # sol_file.write(str(maze_map))
    #     sol_file.write(str([n.id for n in path])+'\n')
    #     sol_file.write('cost = ' + str(cost)+ '\n')
    #     sol_file.write('route = ' + str(route))
