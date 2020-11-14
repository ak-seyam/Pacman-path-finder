from typing import List
from models.graph import Node

def get_total_cost(nodes_list: List[Node]) -> int:
    """
    get nodes list and calculate the total cost of the path in the givin graph
    """
    total_cost = 0
    for i in range(1,len(nodes_list)):
        total_cost += nodes_list[i-1].distance(nodes_list[i])
    return total_cost