from models import Graph, Maze_map, Map_point, Map_el, Location
from flask import Flask, jsonify
from flask import request

import json
import dataclasses
import pickle

from algorithms.A_star import a_star, path_to_distance, a_star_one_target,path_to_points
from algorithms.DFS import dfs_single_target
from algorithms.BFS_sovler import BFS_Solver
from algorithms.BFS import BFS
from algorithms.GFS import GFS
from algorithms.GFS_Solver import GFS_Solver
from utils.informed_multi_target_solver import informed_multi_target_solver


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


def multi_point_path(targets_dict):
    path = []
    for key in targets_dict:
        path += targets_dict[key][:-1]

    return path


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


@app.route("/map/<int:maze_num>/sol/a_star")
def map_sol_a_star(maze_num):
    maze_map = mazes[maze_num]
    start_node = maze_map.get_node_by_map_point(maze_map.player)
    target_node = maze_map.get_node_by_map_point(maze_map.traget[0])

    path, cost = a_star_one_target(start_node, target_node)
    points = path_to_points(path)
    distance = path_to_distance(path)
    return json.dumps({"points": points, "cost": distance}, cls=EnhancedJSONEncoder)


@app.route("/map/<int:maze_num>/sol/dfs")
def map_sol_dfs(maze_num):
    maze_map = mazes[maze_num]

    adjc_dict = maze_map.graph.get_adjacency_dict()
    start_node = maze_map.get_node_by_map_point(maze_map.player)
    target_node = maze_map.get_node_by_map_point(maze_map.traget[0])

    path_ids = dfs_single_target(start_node.id, target_node.id, adjc_dict)
    
    path = [maze_map.graph.nodes[id_] for id_ in path_ids]
    # cost  = path_to_distance(path)
    route = path_to_points(path)
    distance = path_to_distance(path)

    points = route
    return json.dumps({"points": points, "cost": distance}, cls=EnhancedJSONEncoder)


@app.route("/map/<int:maze_num>/sol/bfs")
def map_sol_bfs(maze_num):
    maze_map = mazes[maze_num]
    starting_point = maze_map.get_node_by_map_point(maze_map.player).id

    sol = BFS_Solver(starting_point, maze_map.graph, maze_map)
    BFS(maze_map.graph, starting_point, sol.solver, sol.steps_counter)

    path_dict = sol.get_result()
    path_ids = path_dict[next(iter(path_dict))]
    path = [maze_map.graph.nodes[id_] for id_ in path_ids]

    distance = path_to_distance(path)
    points = path_to_points(path)
    return json.dumps({"points":points,"cost":distance}, cls=EnhancedJSONEncoder)


@app.route("/map/<int:maze_num>/sol/gfs")
def map_sol_gfs(maze_num):
    maze_map = mazes[maze_num]
    starting_point = maze_map.get_node_by_map_point(maze_map.player).id
    graph = maze_map.graph
    sol = GFS_Solver(graph, starting_point)
    informed_multi_target_solver(
        GFS, graph, starting_point, maze_map, sol.solve, sol.steps_counter)
    
    path_dict = sol.get_path()
    
    path_ids = path_dict[next(iter(path_dict))]
    print(path_ids)
    path = [maze_map.graph.nodes[id_] for id_ in path_ids]
    distance = path_to_distance(path)
    points = path_to_points(path)
    return json.dumps({"points": points, "cost": distance}, cls=EnhancedJSONEncoder)


            
@app.route("/map/<int:maze_num>/sol/multi/gfs")
def map_sol_multi(maze_num):
    maze_map = mazes[maze_num]
    starting_point = maze_map.get_node_by_map_point(maze_map.player).id
    graph = maze_map.graph
    sol = GFS_Solver(graph, starting_point)
    informed_multi_target_solver(
        GFS, graph, starting_point, maze_map, sol.solve, sol.steps_counter)

    targets_dict = sol.get_path()
    
    for k in targets_dict.keys():
        path_ids = targets_dict[k]
        path = [maze_map.graph.nodes[id_] for id_ in path_ids]
        points = path_to_points(path)
        targets_dict[k] = points

    targets_ordered = list(targets_dict.keys())
    distance = path_to_distance(path)
    return json.dumps({"points": targets_dict,"order":targets_ordered, "cost": distance}, cls=EnhancedJSONEncoder)

# NOTE for map visit /index.html
if __name__ == "__main__":

    app.run(debug=True)
