from models import Graph, Maze_map


mazes = [
 'bigDots.txt'
,'bigMaze.txt'
,'mediumMaze.txt'
,'mediumSearch.txt'
,'openMaze.txt'
,'smallSearch.txt'
,'tinySearch.txt']


maze_map = Maze_map(f'Maze/{mazes[-1]}')

print(maze_map)
# for i in maze_map.graph.get_adjacency_list():
#     print(i)
# for i in maze_map.node_map():
#     print(i)
