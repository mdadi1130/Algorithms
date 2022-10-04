import sys


class Graph(object):
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)

    def construct_graph(self, nodes, init_graph):
        graph = {}
        for node in nodes:
            graph[node] = {}

        graph.update(init_graph)

        for node, edges in graph.items():
            for adjacent_node, value in edges.items():
                if not graph[adjacent_node].get(node, False):
                    graph[adjacent_node][node] = value

        return graph

    def get_nodes(self):
        return self.nodes

    def get_outgoing_edges(self, node):
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False):
                connections.append(out_node)

        return connections

    def value(self, node1, node2):
        return self.graph[node1][node2]


# Dijkstra's algorithm
def dijkstra(self, graph, start_node):
    unvisited_nodes = list(graph.get_nodes())

    shortest_path = {}

    prev_nodes = {}

    max_val = sys.maxsize
    for node in unvisited_nodes:
        shortest_path[node] = max_val

    shortest_path[start_node] = 0

    while unvisited_nodes:
        current_min_node = None
        for node in unvisited_nodes:
            if current_min_node is None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node

        neighbors = graph.get_outgoing_edges(current_min_node)
        for neighbor in neighbors:
            tentative_val = shortest_path[current_min_node] + graph.value(current_min_node, neighbor)
            if tentative_val < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_val
                prev_nodes[neighbor] = current_min_node

        unvisited_nodes.remove(current_min_node)

    return prev_nodes, shortest_path
