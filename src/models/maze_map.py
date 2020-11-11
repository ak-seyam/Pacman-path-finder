import copy
from .graph import Graph, Node
from .maze_items import Location, Map_el, Map_point, Direction, Path
from typing import List
import math


class Maze_map:

    def __init__(self, path):
        self.layout = self.load_map(path)
        self.hight = len(self.layout)
        self.width = len(self.layout[0])
        # find pathes for every point
        self.layout = self._fill_pathes(self.layout)
        self.player = self.find(Map_el.PLAYER)[0]
        self.traget = self.find(Map_el.TRAGET)
        self._node_id = -1  # so first node_id is 0
        self._edge_id = 999
        self.graph = self.build_graph()

    def _next_node_id(self):
        self._node_id += 1
        return self._node_id

    def _next_edge_id(self):
        self._edge_id += 1
        return self._edge_id

    def load_map(self, path) -> List[List[Map_point]]:
        '''load map point and meta'''
        with open(path) as maze_file:
            maze_map = maze_file.read()
            maze_map = maze_map.split("\n")
            maze_map = [list(row) for row in maze_map]

        self.layout = self._sympol_to_map_point(maze_map)
        return self.layout

    def get_point_by_location(self, location: Location) -> Map_point:
        return self.layout[location.y][location.x]

    def build_graph(self):
        graph = Graph()
        # TODO make adding nodes,edges optional
        # NOTE we can save lots of computation by not adding nodes at all
        # and use the _connected_nodes points in edge insertion
        # NOTE seems there is no need biggiset maze load in no time
        for row in self.layout:
            for point in row:
                if point.is_node():
                    graph.insert_node(self._next_node_id(), point)

        # update the graph with nodes
        # to use later with edges
        self.graph = graph
        # TODO make sure edge note added twice for both direction
        for node in graph.nodes:
            for connected_node in self._connected_nodes(node):
                graph.insert_edge(self._next_edge_id(),
                                  connected_node.id, node.id)

        return graph
    # NOTE why not use location as node id

    def _connected_nodes(self, node: Node) -> List[Node]:
        nodes = []
        available_pathes = node.map_point.available_pathes
        if available_pathes:
            for path in available_pathes:
                next_point =  path.next_node_point()
                if next_point:
                    n = self._get_node_by_location(next_point.location)
                    if n:
                        nodes.append(n)

        return nodes

    def _mark_visited(self, map_point: Map_point):
        loc = map_point.location
        map_point.is_visited = True
        self.layout[loc.y][loc.x] = map_point

    def next_pathes(self, point: Map_point, from_direction: Direction) -> List[Map_point]:
        next_ = []
        if point.is_end_point():
            return next_

        for path in point.available_pathes:
            if path.direction.opposite != from_direction:
                next_.append(path)
        return next_

    def _sympol_to_map_point(self, maze_map: List[List[str]]):
        ''' convert symbol to map point '''
        maze_map = copy.deepcopy(maze_map)
        for row_index, row in enumerate(maze_map):
            for col_index, symbol in enumerate(row):
                map_point = Map_point(Map_el(symbol),
                                      Location(col_index, row_index))
                maze_map[row_index][col_index] = map_point

        return maze_map

    def _fill_pathes(self, maze_map: List[List[Map_point]], in_place=True):
        ''' fill available path for every point in map except for wall points'''

        if not in_place:
            maze_map = copy.deepcopy(maze_map)

        for row_index, row in enumerate(maze_map):
            for col_index, p in enumerate(row):
                if p.content != Map_el.WALL:
                    p.available_pathes = self.available_pathes(p.location)
                    maze_map[row_index][col_index] = p

        return maze_map

    def find(self, content: Map_el):
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
        maze_map = [row.copy() for row in maze_map]
        # maze_map = copy.deepcopy(maze_map)
        for row_index, row in enumerate(maze_map):
            for col_index, point in enumerate(row):
                maze_map[row_index][col_index] = point.content.value+' '

        return maze_map

    def _marked_intersection(self):
        maze = self._map_point_to_sympol(self.layout)
        for row in self.layout:
            for point in row:
                if self.is_intersection(point.location):
                    maze[point.location.y][point.location.x] = '{:<2}'.format(
                        self._get_node_by_location(point.location).id)
        return maze

    def _marked_nodes(self):
        maze = self._map_point_to_sympol(self.layout)
        for row in self.layout:
            for point in row:
                if self.is_node(point.location):
                    maze[point.location.y][point.location.x] = '{:<2}'.format(
                        self._get_node_by_location(point.location).id)

        return maze

    def _get_node_by_location(self, location: Location):
        # TODO may need better approach check note in build graph

        point = self.get_point_by_location(location)
        for node in self.graph.nodes:
            if node.map_point == point:
                return node

    def __str__(self):

        maze = 'original map \n'
        for row in self._map_point_to_sympol(self.layout):
            maze += ''.join(row)+'\n'

        # important points
        maze += 'marked intersection \n'
        for row in self._marked_intersection():
            maze += ''.join(row)+'\n'

        maze += 'marked nodes \n'
        for row in self._marked_nodes():
            maze += ''.join(row)+'\n'

        return maze

    def calculate_distance(self, location_1: Location, location_2: Location):
        return math.sqrt((location_2.x - location_1.x)**2 + (location_2.y - location_1.y)**2)

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

    def nighbors_mat(self, location: Location) -> List[Map_point]:
        ''' array  of nighbors in order [top , right, bottom, left] '''
        return [self.point_in_top(location),
                self.point_in_right(location),
                self.point_in_bottom(location),
                self.point_in_left(location)]

    def available_pathes(self, location) -> List[Path]:
        ''' find free pathes for location '''
        if self.get_point_by_location(location).content == Map_el.WALL:
            return []

        pathes = []
        top, right, bottom, left = self.nighbors_mat(location)

        if top and top.content != Map_el.WALL:  # top
            pathes.append(Path(Direction.UP, top))

        if right and right.content != Map_el.WALL:  # right
            pathes.append(Path(Direction.RIGHT, right))

        if bottom and bottom.content != Map_el.WALL:  # bottom
            pathes.append(Path(Direction.DOWN, bottom))

        if left and left.content != Map_el.WALL:  # left
            pathes.append(Path(Direction.LEFT, left))

        return pathes

    def is_intersection(self, location: Location) -> bool:
        return self.get_point_by_location(location).is_intersection()

    def is_bidirectional(self, location: Location) -> bool:
        return self.get_point_by_location(location).is_bidirectional()

    def is_end_point(self, location: Location) -> bool:
        return self.get_point_by_location(location).is_end_point()

    def is_trget(self, location) -> bool:
        return self.get_point_by_location(location).content == Map_el.TRAGET

    def node_map(self):
        ''' generte a map for each node id and its location'''
        for node in self.graph.nodes:
            yield (node.id, node.map_point.location)

    def is_node(self, location) -> bool:
        return self.get_point_by_location(location).is_node()
