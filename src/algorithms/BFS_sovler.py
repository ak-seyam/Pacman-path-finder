from models import Maze_map

class BFS_Solver():
    """get the parent by reversing the adjacency list"""

    def __init__(self, start_point, graph, maze_map: Maze_map):
        self.starting_point = start_point  # where i'm going to stop from the next target
        self.maze_map = maze_map
        self.graph = graph
        self.visited_targets = {start_point}
        self._res = {self.starting_point:[self.starting_point]}
        self.res = {}

    # nodes_list is a list of nodes that consest of [parent,its children...]
    def solver(self, nodes_list):
        # create pathes for every node by appending to to parents table if node is target add it to res
        self._prepare_res(nodes_list)

    def _prepare_res(self, nodes_list):
        for i in range(1, len(nodes_list)):
            point = nodes_list[i][0]
            parent = nodes_list[0]
            if self._res.get(point):
                if point not in self._res[point]:
                    self._res[point] = self._res[parent] + [point] 
            else :
                self._res[point] = self._res[parent] + [point] 

    def get_all_points_pathes(self):
        return self._res

    def get_result(self):
        res = []
        for target in self.maze_map.traget:
            id = self.maze_map._get_node_by_location(target.location).id
            res.append({id: self._res[id]})
        return res