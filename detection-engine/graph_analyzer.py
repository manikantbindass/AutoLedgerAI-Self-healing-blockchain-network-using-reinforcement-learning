import networkx as nx

class GraphAnalyzer:
    def __init__(self):
        self.graph = nx.DiGraph()

    def add_interaction(self, node_a: str, node_b: str, weight: float = 1.0):
        if self.graph.has_edge(node_a, node_b):
            self.graph[node_a][node_b]['weight'] += weight
        else:
            self.graph.add_edge(node_a, node_b, weight=weight)

    def detect_sybil_clusters(self) -> list:
        if self.graph.number_of_nodes() == 0:
            return []
        undirected = self.graph.to_undirected()
        try:
            cliques = list(nx.find_cliques(undirected))
            sybils = []
            for clique in cliques:
                if len(clique) >= 3:
                    sybils.extend(clique)
            return list(set(sybils))
        except Exception:
            return []
