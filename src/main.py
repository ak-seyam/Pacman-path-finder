from models import Graph, Maze_map, Map_point, Map_el, Location
from algorithms.BFS import BFS
from algorithms.DFS import DFS
from algorithms.GFS import GFS
from algorithms.GFS_Solver import GFS_Solver

mazes = [
 'bigDots.txt'
,'bigMaze.txt'
,'mediumMaze.txt'
,'mediumSearch.txt'
,'openMaze.txt'
,'smallSearch.txt'
,'tinySearch.txt']


maze_map = Maze_map(f'Maze/{mazes[1]}')

# maze_map = Maze_map('Maze/tinySearch.txt')
# print(maze_map)

# BFS(g,9)
starting_point = maze_map.get_node_by_map_point(maze_map.player).id
sol = GFS_Solver(starting_point)
GFS(maze_map.graph,starting_point,maze_map, sol.solve)
print(sol.get_path())
# print("start from 1")
# BFS(g,1)
# print("start from 2")
# BFS(g,2)
print(maze_map)


# print(maze_map)
# for i in maze_map.graph.get_adjacency_list():
#     print(i)
# for i in maze_map.node_map():
#     print(i)


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
