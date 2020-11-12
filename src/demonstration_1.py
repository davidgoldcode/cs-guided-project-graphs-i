"""
You are given an undirected graph with its maximum degree (the degree of a node
 
You need to write a function that can take an undirected graph as its argument
and color the graph legally (a legal graph coloring is when no adjacent nodes
have the same color).

The number of colors necessary to complete a legal coloring is always one more
than the graph's maximum degree.

*Note: We can color a graph in linear time and space. Also, make sure that your
solution can handle a loop in a reasonable way.*
"""
# Definition for a graph node.


colors = ['Yellow', 'Blue', 'Red', 'Green', 'Purple']


class GraphNode:
    def __init__(self, val):
        self.val = val
        self.neighbors = set()
        self.color = None

# O(V * E)


def color_graph(graph, colors):
    # two independent variavles: the number of nodes & the number of connections

    # O(V) where V is the number of vertices/nodes
    for node in graph:
        illegal_colors = set()

    # O(E) where E is the number of connections/edges
        for neighbor in node.neighbors:
            if neighbor.color is not None:
                illegal_colors.add(neighbor.color)

    # O(E) since in the worst case we could color every node a diff color
        for color in colors:
            if color not in illegal_colors:  # O(1) - using set
                node.color = color
                break

    """
    1. Can make every single node a different color
    ### how do we minimize the number of colors used??? 
    ### for the first node, any color is fine - none are colored yet
    ### as we continue iterating through our graph, we need to figure out
    ### what colors are illegal for a given node
    ### we can iterate through a nodes neighbors to see which are colored
    ### build up a set of illegal colors for every node
    ### figure out which color(s) from the color list are not in the illegal set for colors of given node
    ### assign its color to that color 


    """


g1 = GraphNode('G1')
g2 = GraphNode('G2')
g3 = GraphNode('G3')
g4 = GraphNode('G4')
g5 = GraphNode('G5')

g1.neighbors.add(g2)
g1.neighbors.add(g4)
g1.neighbors.add(g3)

g2.neighbors.add(g1)
g2.neighbors.add(g4)
g2.neighbors.add(g5)

g3.neighbors.add(g1)
g3.neighbors.add(g5)
g3.neighbors.add(g4)

g4.neighbors.add(g1)
g4.neighbors.add(g2)
g4.neighbors.add(g3)
g4.neighbors.add(g5)

g5.neighbors.add(g2)
g5.neighbors.add(g3)
g5.neighbors.add(g4)

graph = [g1, g2, g3, g4, g5]
color_graph(graph, colors)

for node in graph:
    print(node.color)
