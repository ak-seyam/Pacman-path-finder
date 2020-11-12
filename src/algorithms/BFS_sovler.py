from models import Maze_map

class BFS_Solver():
    """get the parent by reversing the adjacency list"""

    def __init__(self, start_point, graph, maze_map: Maze_map):
        self.parents_table = {}  # parent table is the reversed version of adj list
        self.starting_point = start_point  # where i'm going to stop from the next target
        self.maze_map = maze_map
        self.graph = graph
        self.visited_targets = {start_point}
        self._res = {self.starting_point:[self.starting_point]}
        self.res = {}

    def find(self,l,value):
        res = -1
        try:
            return l.index(value)
        except :
            return res            
        

    # nodes_list is a list of nodes that consest of [parent,its children...]
    def solver(self, nodes_list):
        # create pathes for every node by appending to to parents table if node is target add it to res
        for i in range(1, len(nodes_list)):
            p = nodes_list[i][0]
            # self._res[p] = list()
            # if self.find(self._res[nodes_list[i][0]],[nodes_list[i][0]]) == -1:
            
            if self._res.get(p):
                if p not in self._res[p]:
                    self._res[p] = self._res[nodes_list[0]] + [p] 
            else :
                self._res[p] = self._res[nodes_list[0]] + [p] 

    def get_result(self):
        res = []
        for target in self.maze_map.traget:
            id = self.maze_map._get_node_by_location(target.location).id
            res.append({id: self._res[id]})
        return res