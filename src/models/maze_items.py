from dataclasses import dataclass
from enum import Enum


class Map_el(Enum):
    WALL = '%'
    PLAYER = 'P'
    TRAGET = '.'
    EMPTY = ' '


@dataclass
class Location:
    x: int
    y: int


@dataclass
class Map_point:
    content: Map_el
    location: Location
