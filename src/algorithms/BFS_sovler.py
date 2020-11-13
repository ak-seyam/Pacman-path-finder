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
        imm_res = {}
        for id in self._res:
            if self.graph.nodes[id].is_target():
                imm_res[id] = self._res[id]
        prev_key = None
        for key in imm_res :
            if prev_key == None:
                prev_key = key
            else:
                for parent_index_in_child in range(len(imm_res[key])-2,-1,-1):
                    if imm_res[key][parent_index_in_child] in imm_res[prev_key] :
                        imm_res[key] = imm_res[key][parent_index_in_child:]
                        break
            prev_key = key
        return imm_res
