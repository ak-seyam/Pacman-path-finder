from models.graph import Node
class GFS_Solver():
    def __init__(self, starting_point):
        self._path = {}
        self._temp_list = []
    def solve(self, node:Node):
        id = node.id
        if not node.is_target():
            self._temp_list.append(id)
        else :
            if id not in self._path.keys():
                self._path[id] = self._temp_list + [id]
                self._temp_list = [id]


    def get_path(self):
        return self._path