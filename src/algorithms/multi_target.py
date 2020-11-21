from utils.prepare_targets import prepare_targets
from algorithms.A_star import parent_list_distance_to_path
from models import TargetNode

def a_star_multi_target(maze_map, starting_node_id):
    current_node_id = starting_node_id
    target_nodes_id = [point.node_id for point in maze_map.traget]
    

    current_node = maze_map.graph.nodes[current_node_id]
    target_nodes = []
    for target in maze_map.traget:
        target_nodes.append(maze_map._get_node_by_location(target.location))

    distance = 0    
    for target_node in target_nodes:
        distance += target_node.heuristics(current_node)

    avg_distance = distance / len(maze_map.traget)
    # avg_distance = 1000

    current_state = TargetNode(current_node_id, target_nodes_id)
    
    

    # TargetNode : (parent,distance_to_node)
    state_parent_distance = {current_state: (None, 0)}

    visited = []
    cost_value = {current_state: 100} # the number doesn't matter
    while len(current_state.remain) > 0:
        connected_targets_cost = prepare_targets(maze_map, current_node_id ,current_state.remain)
        possible_states = []
        for target_id in connected_targets_cost:
            if target_id in current_state.remain :
                new_remain = current_state.remain.copy()
                new_remain.remove(target_id)
                
                possible_states.append(TargetNode(
                    target_id, new_remain))
            


        # parent, parent_distance = state_parent_distance[current_state]
        # if parent:
        parent, distance_to_current_state = state_parent_distance[current_state]
        
        for state in possible_states:
            if state not in visited:
                distance = distance_to_current_state + connected_targets_cost[state.current]
                # target_node = maze_map.graph.nodes[state.current]
                # current_node = maze_map.graph.nodes[current_state.current]
                # heuristics = current_node.heuristics(target_node)
                heuristics = len(state.remain)*avg_distance
                cost = distance + heuristics

                old_cost = cost_value.get(state,None)
                if old_cost is not None:
                    if cost < old_cost:
                        cost_value[state] = cost
                        state_parent_distance[state] = (current_state, distance)
                else:
                    cost_value[state] = cost
                    state_parent_distance[state] = (
                        current_state, distance)

        cost_value.pop(current_state, None)
        visited.append(current_state)

        if len(current_state.remain) < 1:
            print("small")
        # if len(cost_value) == 0:
            # return None
        current_state =  min(
            cost_value.keys(), key=lambda k: cost_value[k])

    visited.append(current_state)

    path = parent_list_distance_to_path(state_parent_distance, current_state)
    path_node_id = []
    for t_node in path:
        path_node_id.append(t_node.current)
    return path_node_id


def GFS_multi(maze_map, starting_node_id: int):
    current_node = maze_map.graph.get_node_by_id(starting_node_id)
    target_nodes = []
    for target in maze_map.traget:
        target_nodes.append(maze_map._get_node_by_location(target.location))

    moving_map_nodes = {}
    cost_map_nodes = {}
    # TODO sort targets
    # list_heuristic = [(t.id, t.heuristics(current_node)) for t in target_nodes]

    n_targets = len(target_nodes)
    for _ in range(n_targets):
        target_node = min(
            target_nodes, key=lambda target: current_node.heuristics(target))
        moving_map_nodes[target_node], cost_map_nodes[target_node] = a_star_one_target(
            current_node, target_node)
        current_node = target_node
        target_nodes.remove(target_node)

    moving_map = {}
    cost_map = {}
    for k in moving_map_nodes.keys():
        moving_map[k.id] = [n.id for n in moving_map_nodes[k] if n is not None]
        cost_map[k.id] = cost_map_nodes[k]

    return moving_map, cost_map
