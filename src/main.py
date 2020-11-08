from models.graph import Graph
from models.maze_map import Maze_map



maze_map = Maze_map('Maze/tinySearch.txt')

print(maze_map)
for i in maze_map.graph.get_adjacency_list():
    print(i)
for i in maze_map.node_map():
    print(i)

