from __future__ import annotations
from dataclasses import dataclass
from enum import Enum
from typing import List


class Map_el(Enum):
    WALL = '%'
    PLAYER = 'P'
    TRAGET = '.'
    EMPTY = ' '


class Direction(Enum):
    UP = 'u'
    RIGHT = 'r'
    DOWN = 'b'
    LEFT = 'l'
    def opposite(self):
        ''' return opposite direction

        >>> Direction.UP.opposite() == Direction.DOWN
        True
        '''
        opposite = None
        opposite = Direction.DOWN if self == Direction.UP else opposite
        opposite = Direction.UP if self == Direction.DOWN else opposite
        opposite = Direction.RIGHT if self == Direction.LEFT else opposite
        opposite = Direction.LEFT if self == Direction.RIGHT else opposite

        return opposite

@dataclass
class Location:
    x: int
    y: int


@dataclass
class Path:
    start: Map_point
    start_direction: Direction
    # end: Map_point

@dataclass
class Map_point:
    content: Map_el
    location: Location = Location(-1,-1)
    available_pathes: List[Path] = None
    def is_bidirectional(self):
        ''' test if point is in one way road '''
        return len(self.available_pathes) == 2 and self.content != Map_el.WALL
    def is_intersection(self):
        ''' if intersection
        
        >>> m1 = Map_point(Map_el.EMPTY, available_pathes = [1,2])
        >>> m1.is_intersection()
        False
        >>> m2 = Map_point(Map_el.EMPTY, Location(0,0), [])
        >>> m3 = Map_point(Map_el.EMPTY, Location(0,0), [m1,m2,m2])
        >>> m3.is_intersection()
        True
        '''
        return len(self.available_pathes) >= 3 and self.content != Map_el.WALL
    def is_end_point(self):
        return len(self.available_pathes) == 1 and self.content != Map_el.WALL


if __name__ == "__main__":
    import doctest
    doctest.testmod()
