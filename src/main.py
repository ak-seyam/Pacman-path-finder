from models import Graph, Maze_map, Map_point, Map_el, Location
from algorithms.BFS import BFS


mazes = [
 'bigDots.txt'
,'bigMaze.txt'
,'mediumMaze.txt'
,'mediumSearch.txt'
,'openMaze.txt'
,'smallSearch.txt'
,'tinySearch.txt']


maze_map = Maze_map(f'Maze/{mazes[-1]}')

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
print(maze_map)


# for i in maze_map.graph.get_adjacency_list():
#     print(i)
# for i in maze_map.node_map():
#     print(i)
