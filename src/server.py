from models import Graph, Maze_map, Map_point, Map_el, Location
from flask import Flask, jsonify
import json
import dataclasses
import pickle


from enum import Enum
app = Flask(__name__)

mazes = [
    'bigDots.txt', 'bigMaze.txt', 'mediumMaze.txt', 'mediumSearch.txt', 'openMaze.txt', 'smallSearch.txt', 'tinySearch.txt']


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


@app.route('/map')
def map():
    map_ = mazes[-1]
    maze = Maze_map(f'Maze/{map_}')
    # j = ""
    # for row in maze.layout:
    # j += json.dumps(row , cls=EnhancedJSONEncoder)
    height = len(maze.layout)
    width = len(maze.layout[0])
    return json.dumps({"map": maze.all_points(),
                       "height": height,
                       "width": width},
                      cls=EnhancedJSONEncoder)
    # return pickle.dumps(maze.layout)

# NOTE for map visit /index.html
if __name__ == "__main__":

    app.run(debug=True)
