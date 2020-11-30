from models import Graph, Maze_map, Map_point, Map_el, Location
from algorithms.BFS import BFS
from algorithms.DFS import dfs_single_target
from algorithms.GFS import GFS
from algorithms.GFS_Solver import GFS_Solver
from algorithms.BFS_sovler import BFS_Solver
from utils.informed_multi_target_solver import informed_multi_target_solver
from utils.prepare_targets import prepare_targets
from algorithms.A_star import  path_to_distance, a_star_one_target, path_to_points
from algorithms.multi_target import a_star_multi_target
# from algorithms.A_star import a_star, path_to_distance, a_star_one_target, path_to_points
from utils.search import search_type, search
import os 

# mazes = [
#     'bigDots.txt', 'bigMaze.txt', 'mediumMaze.txt', 'mediumSearch.txt', 'openMaze.txt', 'smallSearch.txt', 'tinySearch.txt']

mazes = [
    'bigMaze.txt', 'mediumMaze.txt', 'openMaze.txt', 'bigDots.txt','mediumSearch.txt', 'smallSearch.txt', 'tinySearch.txt']

# NOTE testing common search logic
for i in search_type:
    for j in range(7):
        if j > 2 and i == search_type.DFS:
            break
        maze_name = mazes[j]
        maze_map = Maze_map(f'Maze/{maze_name}')

        search_type_name = i.name

        # print("Testing...")
        print('search type is: ',i)
        s = search(i, maze_map)
        path = s.get_path()
        # print(f"path saved in sol/{search_type_name}/{mazes[j]}")
        cost = s.get_cost()
        # print(f"cost saved in sol/{search_type_name}/{mazes[j]}")
        expansion = s.get_expansion()
        # print(f"expansion saved in sol/{search_type_name}/{mazes[j]}")
        number_of_expanded_nodes = s.get_number_of_expanded_nodes()
        # print(
            # f"number_of_expanded_nodes saved in sol/{search_type_name}/{mazes[j]}")

        if not os.path.exists(f'sol/{search_type_name}'):
            os.makedirs(f'sol/{search_type_name}')
        
        with open(f'sol/{search_type_name}/{mazes[j]}', 'w') as sol_file:
                # sol_file.write(str(maze_map))
            sol_file.write('path = ' + str(path) + '\n')
            sol_file.write('cost = ' + str(cost) + '\n')
            sol_file.write('expansion = ' + str(expansion) + '\n')
            sol_file.write('number_of_expanded_nodes = ' + str(number_of_expanded_nodes) + '\n')
                
        print(f"saved sol/{search_type_name}/{mazes[j]}")


def multi_point_path(targets_dict):
    path = []
    for key in targets_dict:
        path += targets_dict[key][:-1]

    return path

# maze_map = Maze_map(f'Maze/{mazes[-2]}')

# starting_point = maze_map.get_node_by_map_point(maze_map.player).id
# res = a_star_multi_target(maze_map , maze_map.player.node_id)
# print('a_star ',res)
# path = multi_point_path(res)
# print('path', path)
# res_nodes = [maze_map.graph.nodes[id_] for id_ in path]
# print("cost", path_to_distance(res_nodes))

# print(maze_map)

# # GFS solver
# graph = maze_map.graph
# sol = GFS_Solver(graph, starting_point)
# informed_multi_target_solver(
#     GFS, graph, starting_point, maze_map, sol.solve, sol.steps_counter)
# print('gready', sol.get_path())
# print('path', multi_point_path(sol.get_path()))
# print('result expansion', sol.expansion)
# print('#hits: ', sol.num_hits)
# print('total cost', sol.res_path_cost())

# targets_ids = [t.node_id for t in maze_map.traget]
# print(prepare_targets(maze_map, 0, [15,20,2,8,19]))
# >>> {2: 0, 8: 1, 19: 3, 15: 4} for tiny
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
