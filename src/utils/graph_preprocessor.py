from models.graph import GraphStructureError
def graph_algorithm(preprocessor=None):
    """
        a graph decorator which checks for graph validity and do preprocessing 
        if supplied
        NOTE: the preprocessor is function that return a preprocessed graph
    """
    def decorator(function):
        def wrapper(*args, **kwargs):
            graph = args[0]
            if len(graph.nodes) and not len(graph.edges):
                raise GraphStructureError("all nodes are not connected")
            if preprocessor :
                graph = preprocessor(graph) 
            result = function(graph)
            return result
        return wrapper
    return decorator