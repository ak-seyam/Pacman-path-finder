from models import Graph, Maze_map, Map_point, Map_el, Location
from flask import Flask, jsonify
from flask import request

import json
import dataclasses
import pickle

from algorithms.A_star import a_star, path_to_distance, a_star_one_target,path_to_points


from enum import Enum
app = Flask(__name__)

mazes_files = [
    'bigDots.txt', 'bigMaze.txt', 'mediumMaze.txt', 'mediumSearch.txt', 'openMaze.txt', 'smallSearch.txt', 'tinySearch.txt']


mazes = [Maze_map(f'Maze/{map_}') for map_ in mazes_files]


class EnhancedJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Map_point):
            return {"content": o.content,
                    "location": o.location,
                    "node_id": o.node_id
                    }
        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        if isinstance(o, Enum):
            return o.name

        return super().default(o)


@app.route('/')
def hello():
    return 'hello'


@app.route('/map/<int:maze_num>')
def map(maze_num):
    maze = mazes[maze_num]
    height = len(maze.layout)
    width = len(maze.layout[0])
    return json.dumps({"map": maze.all_points(),
                       "height": height,
                       "width": width},
                      cls=EnhancedJSONEncoder)
    
# @app.route("/map/path")
# def map_path():
    # from_node_id = int(request.args.get('from'))
    # to_node_id = request.args.get('to_node')
    # from_node = maze.graph.get_node_by_id(from_node_id)

    # to_node = maze.graph.get_node_by_id(to_node_id)
    # return json.dumps(from_node.map_point.route_to_node_points(), cls=EnhancedJSONEncoder)


@app.route("/map/<int:maze_num>/sol")
def map_sol(maze_num):
    maze_map = mazes[maze_num]
    start_node = maze_map.get_node_by_map_point(maze_map.player)
    target_node = maze_map.get_node_by_map_point(maze_map.traget[0])

    path, cost = a_star_one_target(start_node, target_node)
    points = path_to_points(path)
    return json.dumps(points , cls=EnhancedJSONEncoder)


# NOTE for map visit /index.html
if __name__ == "__main__":

    app.run(debug=True)
