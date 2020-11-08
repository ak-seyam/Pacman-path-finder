import copy
from models.graph import Graph
from models.maze_items import Location, Map_el, Map_point

class Maze_map:

    def __init__(self, path):
        self.layout = self.load_map(path)
        self.hight = len(self.layout)
        self.width = len(self.layout[0])
        self.player = self.find(Map_el.PLAYER)
        self.traget = self.find(Map_el.TRAGET)
        self.graph = self.build_graph()

    def load_map(self, path) -> Map_point:
        with open("Maze/tinySearch.txt") as maze_file:
            maze_map = maze_file.read()
            maze_map = maze_map.split("\n")
            maze_map = [list(row) for row in maze_map]



        self.layout = self._sympol_to_map_point(maze_map)
        return self.layout

    def get_point_by_location(self, location: Location) -> Map_point:
        return self.layout[location.y][location.x]
    
    def build_graph(self):
        graph = Graph()
        counter_id = 0
        for row in self.layout:
            for point in row:
                graph.insert_node(counter_id, point)

        # TODO find edges
        # 1. start from player postion 
        # 2. use x-axis and y-axis to find @next_node
        # 3. measure distance 
        # 4. add edge 
        # 5. contenue with next from @next_nodes at [2]
        return graph

    
    
    def _sympol_to_map_point(self,maze_map):
        maze_map = copy.deepcopy(maze_map)
        for row_index, row in enumerate(maze_map):
            for col_index, symbol in enumerate(row):
                map_point = Map_point(Map_el(symbol),
                                      Location(col_index, row_index))
                maze_map[row_index][col_index] = map_point
        
        return maze_map
    
    def find(self, content : Map_el):
        res = []
        for row in self.layout:
            for point in row:
                if point.content == content:
                    res.append(point)
        return res

    def _map_point_to_sympol(self, maze_map):
        ''' convert a Map_point map to Sympol
        Args: 
            maze_map List<Map_point> 
        '''
        maze_map = copy.deepcopy(maze_map)
        for row_index, row in enumerate(maze_map):
            for col_index, point in enumerate(row):
                maze_map[row_index][col_index] = point.content.value

        return maze_map

    def _marked_nodes(self):
        maze = self._map_point_to_sympol(self.layout)
        
        for row in self.layout:
            for point in row:
                if self.is_intersection(point.location):
                    maze[point.location.y][point.location.x] = '*'
                if self.is_end_point(point.location):
                    maze[point.location.y][point.location.x] = '^'

        return maze

    def __str__(self):

        maze = 'original map \n'
        for row in self._map_point_to_sympol(self.layout):
            maze += ''.join(row)+'\n'

        # important points 
        maze += 'marked map \n'
        for row in self._marked_nodes():
            maze += ''.join(row)+'\n'

        return maze


    def point_in_top(self, location: Location) -> Map_point:
        if location.y == 0:
            return None
        else:
            return self.get_point_by_location(Location(location.x, location.y-1))

    def point_in_bottom(self, location: Location) -> Map_point:
        if location.y == self.hight-1:
            return None
        else:
            return self.get_point_by_location(Location(location.x, location.y+1))

    def point_in_right(self, location: Location) -> Map_point:
        if location.x == self.width-1:
            return None
        else:
            return self.get_point_by_location(Location(location.x+1, location.y))

    def point_in_left(self, location: Location) -> Map_point:
        if location.x == 0:
            return None
        else:
            return self.get_point_by_location(Location(location.x-1, location.y))

    def nighbors_mat(self, location: Location):
        ''' array  of nighbors in order [top , right, bottom, left] '''
        return [self.point_in_top(location),
                self.point_in_right(location),
                self.point_in_bottom(location),
                self.point_in_left(location)]

    def is_intersection(self, location: Location) -> bool:
        if self.get_point_by_location(location).content == Map_el.WALL:
            return False
        
        available_pathes = 0
        for point in self.nighbors_mat(location):
            if point is not None and point.content !=Map_el.WALL:
                available_pathes += 1
        
        return available_pathes >= 3


    def is_end_point(self, location: Location) -> bool:
        if self.get_point_by_location(location).content == Map_el.WALL:
            return False
            
        blocked_pathes = 0
        for point in self.nighbors_mat(location):
            if point is None or point.content == Map_el.WALL:
                blocked_pathes +=1
        
        return blocked_pathes >= 3

    def is_trget(self, location) -> bool:
        return self.get_point_by_location(location).content == Map_el.TRAGET
