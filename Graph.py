import math
from node import *


class Graph:

    def __init__(self) -> None:
        """Constructor for building a graph
        """
        self.nodes = {}

        #define and start and goal node names
        #the same needs to be used in the graph creation
        self.start_node_name = "xs"
        self.goal_node_name = "xg"

        #Create the graph using the node objects
        #Ex node creation: 
        #   node(node_name, {parent:action_cost, ...}, G, rhs, heuristc_cost_to_come)

        #Add created nodes into the node dictionary
        self.nodes["xs"] = node("xs", [], math.inf, math.inf, 0)
        self.nodes["xg"] = node("xg", {"x4":1, "x7": 1, "x8": 1}, math.inf, 0, 5)

        self.nodes["x8"] = node("x8", {"xs":7}, math.inf, math.inf, 1)
        self.nodes["x7"] = node("x7", {"x6":6}, math.inf, math.inf, 3)
        self.nodes["x6"] = node("x6", {"x5":1}, math.inf, math.inf, 2)
        self.nodes["x5"] = node("x5", {"x1":1, "xs":13}, math.inf, math.inf, 1)
        self.nodes["x4"] = node("x4", {"x3":1}, math.inf, math.inf, 8)
        self.nodes["x3"] = node("x3", {"x2":1}, math.inf, math.inf, 6)
        self.nodes["x2"] = node("x2", {"x1":1}, math.inf, math.inf, 5)
        self.nodes["x1"] = node("x1", {"xs":1}, math.inf, math.inf, 1)

        