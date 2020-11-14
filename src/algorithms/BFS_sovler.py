from models import Maze_map

class BFS_Solver():
    """get the parent by reversing the adjacency list"""

    def __init__(self, start_point, graph, maze_map: Maze_map):
        self.starting_point = start_point  # where i'm going to stop from the next target
        self.maze_map = maze_map
        self.graph = graph
        self._res = {self.starting_point:[self.starting_point]}
        self.res = {}
        self.steps = 0
        self.expansion = []

    # nodes_list is a list of nodes that consest of [parent,its children...]
    def solver(self, nodes_list):
        # create pathes for every node by appending to to parents table if node is target add it to res
        self.expansion.append(nodes_list[0])
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
        targets_table = {}
        for id in self._res:
            if self.graph.nodes[id].is_target():
                targets_table[id] = self._res[id]
        prev_key = None
        for key in targets_table :
            if prev_key == None:
                prev_key = key
            else:
                for ancestor_index_c_list in range(len(self._res[key])-2,-1,-1):
                    ancestor_index = self._res[key][ancestor_index_c_list]
                    if ancestor_index in self._res[prev_key] :
                        ancestor_index_p = self._res[prev_key].index(ancestor_index)
                        prev_list_portion = self._res[prev_key][ancestor_index_p+1:]
                        prev_list_portion.reverse()
                        targets_table[key] = prev_list_portion + self._res[key][ancestor_index_c_list:]
                        break
            prev_key = key
        return targets_table

    def steps_counter(self):
        self.steps += 1