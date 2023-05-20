import math

#Class defines the node type
class node:
    def __init__(self, name, parents_links, G, rhs, C) -> None:
        """constructor for building a node

        Args:
            name (string): name of the node
            parents_links (Disctionary): parent node and respective action cost
            G (int): Cost to Goal
            rhs (int): one step look ahead cost
            C (int): heuristic cost to come
        """
        self.name = name
        self.parent = parents_links
        self.G = G
        self.rhs = rhs
        self.C = C
        self.state_action = {}
        self.min_action = None
        self.Key1 = math.inf
        self.Key2 = math.inf

    def print(self, pretext = ""):
        """Print funciton for the node

        Args:
            pretext (str, optional): optional prefix. Defaults to "".
        """
        data = f"{pretext} {self.name} G : {self.G} rhs : {self.rhs} C = {self.C}"
        data = data.replace("inf", "∞")
        print(data)