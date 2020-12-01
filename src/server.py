from models import Graph, Maze_map, Map_point, Map_el, Location
from flask import Flask, jsonify
from flask import request

import json
import dataclasses
import pickle

from utils.path_utils import path_id_to_points, path_to_points, multi_point_path
from algorithms.A_star import path_to_distance, a_star_one_target
from algorithms.DFS import dfs_single_target
from algorithms.BFS_sovler import BFS_Solver
from algorithms.BFS import BFS
from algorithms.GFS import GFS
from algorithms.GFS_Solver import GFS_Solver
from utils.informed_multi_target_solver import informed_multi_target_solver
from algorithms.multi_target import a_star_multi_target
from utils.search import search_type, search


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
    

@app.route("/map/<int:maze_num>/path")
def map_path(maze_num):
    from_node_id = int(request.args.get('from'))
    to_node_id = request.args.get('to_node')
    from_node = mazes[maze_num].graph.get_node_by_id(from_node_id)

    to_node = mazes[maze_num].graph.get_node_by_id(to_node_id)
    return json.dumps(from_node.map_point.route_to_node_points(), cls=EnhancedJSONEncoder)


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
    path = [maze_map.graph.nodes[id_] for id_ in path_ids]
    distance = path_to_distance(path)
    points = path_to_points(path)
    return json.dumps({"points": points, "cost": distance}, cls=EnhancedJSONEncoder)

# # TODO import from path utils
# def multi_point_path(targets_dict):
#     path = []
#     for key in targets_dict:
#         path += targets_dict[key][:-1]

#     return path



@app.route("/map/<int:maze_num>/sol/multi/gfs")
def map_sol_multi(maze_num):
    maze_map = mazes[maze_num]
    starting_point = maze_map.get_node_by_map_point(maze_map.player).id
    graph = maze_map.graph
    sol = GFS_Solver(graph, starting_point)
    informed_multi_target_solver(
        GFS, graph, starting_point, maze_map, sol.solve, sol.steps_counter)

    targets_dict = sol.get_path()
    # targets_dict.keys()

    targets_ordered = list(targets_dict.keys())

    distance = sol.res_path_cost()

    #convert to points
    for k in targets_dict.keys():
        path_ids = targets_dict[k]
        path = [maze_map.graph.nodes[id_] for id_ in path_ids]
        points = path_to_points(path)
        targets_dict[k] = points


    return json.dumps({"points": targets_dict,"order":targets_ordered, "cost": distance}, cls=EnhancedJSONEncoder)


@app.route("/map/<int:maze_num>/sol/multi/a_star")
def map_sol_multi_a_star(maze_num):
    maze_map = mazes[maze_num]
    starting_point = maze_map.get_node_by_map_point(maze_map.player).id

    targets_dict = a_star_multi_target(maze_map, maze_map.player.node_id)

    targets_ordered = list(targets_dict.keys())
    path = multi_point_path(targets_dict)
    res_nodes = [maze_map.graph.nodes[id_] for id_ in path]
    distance = path_to_distance(res_nodes)

    #convert to points
    for k in targets_dict.keys():
        path_ids = targets_dict[k]
        path = [maze_map.graph.nodes[id_] for id_ in path_ids]
        points = path_to_points(path)
        targets_dict[k] = points

    return json.dumps({"points": targets_dict, "order": targets_ordered, "cost": distance}, cls=EnhancedJSONEncoder)


@app.route("/map/<int:maze_num>/sol/single/")
def generic_solver_single(maze_num):    
    maze_map = mazes[maze_num]
    selected_type = request.args.get('search_type')
    # change string to enum
    selected_type = search_type.A_Star if selected_type == "a_star" else selected_type
    selected_type = search_type.DFS if selected_type == "dfs" else selected_type
    selected_type = search_type.BFS if selected_type == "bfs" else selected_type
    selected_type = search_type.GFS if selected_type == "gfs" else selected_type

    s = search(selected_type, maze_map)

    path = list(s.get_path().values())[0]
    distance = s.get_cost()
    points = path_id_to_points(maze_map, path)
    # print(path)
    # distance = path_to_distance(path)
    return json.dumps({"points": points, "cost": distance}, cls=EnhancedJSONEncoder)

@app.route("/map/<int:maze_num>/expand/")
def epander_solver(maze_num):    
    maze_map = mazes[maze_num]
    selected_type = request.args.get('search_type')
    # change string to enum
    selected_type = search_type.A_Star if selected_type == "a_star" else selected_type
    selected_type = search_type.DFS if selected_type == "dfs" else selected_type
    selected_type = search_type.BFS if selected_type == "bfs" else selected_type
    selected_type = search_type.GFS if selected_type == "gfs" else selected_type

    s = search(selected_type, maze_map)

    expantion = s.get_expansion()
    distance = s.get_cost()
    # points = path_id_to_points(maze_map, path)
    # print(path)
    # distance = path_to_distance(path)
    return json.dumps({"expantion": expantion, "cost": distance}, cls=EnhancedJSONEncoder)



@app.route("/map/<int:maze_num>/sol/multi/")
def generic_solver_multi(maze_num):
    maze_map = mazes[maze_num]
    selected_type = request.args.get('search_type')
    # change string to enum
    selected_type = search_type.A_Star if selected_type == "a_star" else selected_type
    selected_type = search_type.DFS if selected_type == "dfs" else selected_type
    selected_type = search_type.BFS if selected_type == "bfs" else selected_type
    selected_type = search_type.GFS if selected_type == "gfs" else selected_type

    s = search(selected_type, maze_map)

    targets_dict = s.get_path()
    distance = s.get_cost()
    targets_ordered = list(targets_dict.keys())
    path = multi_point_path(targets_dict)
    
    # points = path_id_to_points(maze_map, path)

    for k in targets_dict.keys():
        path_ids = targets_dict[k]
        path = [maze_map.graph.nodes[id_] for id_ in path_ids]
        points = path_to_points(path)
        targets_dict[k] = points



    return json.dumps({"points": targets_dict, "order": targets_ordered, "cost": distance}, cls=EnhancedJSONEncoder)


# NOTE for map visit /index.html
if __name__ == "__main__":

    app.run(debug=True)
