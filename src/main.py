from models import Graph, Maze_map, Map_point, Map_el, Location
from algorithms.BFS import BFS


class BFS_Solver():
    """get the parent by reversing the adjacency list"""

    def __init__(self, start_point, graph, maze_map: Maze_map):
        self.parents_table = {}  # parent table is the reversed version of adj list
        self.starting_point = start_point  # where i'm going to stop from the next target
        self.maze_map = maze_map
        self.graph = graph
        self.visited_targets = []

    # nodes_list is a list of nodes that consest of [parent,its children...]
    def solver(self, nodes_list):
        for i in range(1, len(nodes_list)):
            row = self.parents_table.get(nodes_list[i])
            if not row:  # prepare the row in other words create the parents list
                self.parents_table[nodes_list[i][0]] = []
                row = self.parents_table[nodes_list[i][0]]
            row.append(nodes_list[0])  # add the parent to children rows
            # if maze_map.is_trget(self.graph.nodes[nodes_list[i][0]].map_point.location):
            #     # if the node_list[0] is neither target nor self.previous_parent
            #     # check for parent table [node_list[0]][0] till you fill
            #     # that condition this send the res as the second param
            #     started_from = nodes_list[0]
            #     while not (maze_map.is_trget(self.graph.nodes[started_from].map_point.location) or started_from == self.previous_target):
            #         started_from = self.parents_table[started_from][0]
            #     print(self._build_path(nodes_list[i][0], started_from))
        if self.maze_map.is_trget(self.graph.nodes[nodes_list[0]].map_point.location):
            starting_point = self.starting_point
            if len(self.visited_targets) :
                starting_point = self.parents_table[nodes_list[0]][0]
            print(self._build_path(nodes_list[0],starting_point))
    def _build_path(self, target, started_from):
        """
            This should return the path from the current target to the self.previous target
            and delete the parents accordingly when it finish it should change the previous target to
            the current one and returns key value of the path
        """
        res_list = []
        index = target
        while index != started_from:
            # move to the previous parent
            nu_index = self.parents_table[index][0]
            del self.parents_table[index][0]
            res_list.insert(0, index)
            index = nu_index
        res_list.insert(0, started_from)
        # self.previous_target = target # start from the new target
        self.visited_targets.append(target)
        return {target: res_list}


mazes = [
    'bigDots.txt', 'bigMaze.txt', 'mediumMaze.txt', 'mediumSearch.txt', 'openMaze.txt', 'smallSearch.txt', 'tinySearch.txt']


maze_map = Maze_map(f'Maze/{mazes[-1]}')

# maze_map = Maze_map('Maze/tinySearch.txt')
# print(maze_map)
g = Graph()
g.insert_edge(0, 0, 1)
# g.insert_edge(1,1,2)
g.insert_edge(2, 2, 0)
print("start from 0")
sol = BFS_Solver(9, g, maze_map)
BFS(g, 9, sol.solver)
# print("start from 1")
# BFS(g,1)
# print("start from 2")
# BFS(g,2)
print(maze_map)


# for i in maze_map.graph.get_adjacency_list():
#     print(i)
# for i in maze_map.node_map():
#     print(i)

# Solver code
