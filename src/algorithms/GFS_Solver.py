from models.graph import Node
from utils.get_total_cost import get_total_cost


class GFS_Solver():
    def __init__(self, graph ,starting_point):
        self._path = {}
        self._temp_list = []
        self.expansion = [starting_point]
        self.steps = 0
        self._traversed_nodes = []
        self.graph = graph
    def solve(self, node: Node):
        id = node.id
        self._traversed_nodes.append(id)
        if self.expansion[-1] != id:
            self.expansion.append(id)
        if not node.is_target():
            self._temp_list.append(id)
        else:
            if id not in self._path.keys():
                self._path[id] = self._temp_list + [id]
                self._temp_list = [id]

    def get_path(self):
        return self._path

    def steps_counter(self):
        self.steps += 1
    
    def total_cost(self):
        nodes = [self.graph.nodes[node] for node in self._traversed_nodes]
        return get_total_cost(nodes)