from models.graph import Node
class GFS_Solver():
    def __init__(self, starting_point):
        self._path = [starting_point]
    
    def solve(self, node:Node):
        if self._path[-1] != node.id:
            self._path.append(node.id)

    def get_path(self):
        return {self._path[-1]:self._path}