from models.graph import Graph
from models.maze_map import Maze_map, Map_point, Map_el, Location
from algorithms.BFS import BFS



# maze_map = Maze_map('Maze/tinySearch.txt')
# print(maze_map)
g = Graph()
g.insert_edge(0,0,1)
# g.insert_edge(1,1,2)
g.insert_edge(2,2,0)
print("start from 0")
BFS(g,0)
# print("start from 1")
# BFS(g,1)
# print("start from 2")
# BFS(g,2)