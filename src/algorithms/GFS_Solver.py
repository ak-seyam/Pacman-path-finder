from models.graph import Node
from algorithms.A_star import path_to_distance


class GFS_Solver():
    def __init__(self, graph ,starting_point):
        self._path = {}
        self._temp_list = []
        self.expansion = [starting_point]
        self.num_hits = 0
        self._visited_pois = [starting_point]
        self.graph = graph
    def solve(self, node: Node):
        id = node.id
        self.expansion.append(id)
        if id in self._temp_list: # NOTE don't calculate the revolving back steps
            id_index= self._temp_list.index(id)
            del self._temp_list[id_index:]
        self._temp_list.append(id)
        if node.is_target() and id not in list(self._path.keys()):
            self._path[id] = self._temp_list[:]
            self._temp_list = []

    def get_path(self):
        return self._path

    def steps_counter(self):
        self.num_hits += 1

    def res_path_cost(self):
        distance = 0
        for key in self._path:
            imm_nodes = [self.graph.nodes[id] for id in self._path[key]]
            distance += path_to_distance(imm_nodes)       
        return distance