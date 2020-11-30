from models import Maze_map
from algorithms.A_star import path_to_distance


class BFS_Solver():
    """get the parent by reversing the adjacency list"""

    def __init__(self, start_point, graph, maze_map: Maze_map):
        self.starting_point = start_point  # where i'm going to stop from the next target
        self.maze_map = maze_map
        self.graph = graph
        self._res = {self.starting_point: [self.starting_point]} # _res is all the visited nodes
        self.res = {}
        self.num_hits = 0
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
            else:
                self._res[point] = self._res[parent] + [point]

    def get_all_points_pathes(self):
        # get all the traversed points including the one non participating in the result
        return self._res

    def get_result(self):
        for id in self._res:
            if self.graph.nodes[id].is_target():
                self.res[id] = self._res[id]
        prev_key = None
        for key in self.res:
            if prev_key == None:
                prev_key = key
            else:
                for ancestor_index_c_list in range(len(self._res[key])-2, -1, -1):
                    ancestor_index = self._res[key][ancestor_index_c_list]
                    if ancestor_index in self._res[prev_key]:
                        ancestor_index_p = self._res[prev_key].index(
                            ancestor_index)
                        prev_list_portion = self._res[prev_key][ancestor_index_p+1:]
                        prev_list_portion.reverse()
                        self.res[key] = prev_list_portion + \
                            self._res[key][ancestor_index_c_list:]
                        break
            prev_key = key
        return self.res

    def clean(self):
        self._res = {} # clean all nodes
        self.res = {} # clean result
        self.num_hits = 0 # zeroing number of hits
        self.expansion = [] # cleaning expansion


    def steps_counter(self):
        self.num_hits += 1

    def res_path_cost(self):
        distance = 0
        for key in self.res:
            imm_nodes = [self.graph.nodes[id] for id in self.res[key]]
            distance += path_to_distance(imm_nodes)
        return distance
