from models.graph import Graph

def prepare_targets(graph: Graph, starting_node_id):
    visited_nodes = set()
    # visited_targets = {starting_node_id}
    adjacency_dict = graph.get_adjacency_dict()
    nodes_queue = [starting_node_id]
    res = []
    while len(nodes_queue):
        node = nodes_queue.pop(0)  # remove the first element, FIFO
        if node not in visited_nodes:
            visited_nodes.add(node)
            if not graph.nodes[node].is_target():
                # visited_targets.add(node)
                connections = adjacency_dict.get(node)
                # nodes_queue.extend(connections)
                if connections:
                    for connection in connections:
                        # add the to index to nodes queue
                        nodes_queue.append(connection[0])
            else :
                res.append(node)
    return res
