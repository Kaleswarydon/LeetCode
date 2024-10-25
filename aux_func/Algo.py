from collections import defaultdict

####################################### HELPERS #######################################

def make_edge_list(src_list, dest_list, weight_list):
    assert len(src_list) == len(dest_list) == len(weight_list)
    return [[src_list[i], dest_list[i], weight_list[i]] for i in range(len(src_list))]


def make_edge(a, b, directed: bool=False):
    return (a, b) if directed else frozenset({a, b})

##############################################################################

#-----------------------------------------------------------------------------

####################################### ALGOS #######################################

def floyd_warshall(edges, directed=False):
    dist = defaultdict(lambda: float("inf"))
    vertices = set()
    for src, dest, weight in edges:
        dist[make_edge(src, dest, directed)] = min(weight, dist[make_edge(src, dest, directed)])
        dist[make_edge(src, src, directed)] = 0
        dist[make_edge(dest, dest, directed)] = 0
        vertices.update({src, dest})
    for k in vertices:
        for i in vertices:
            for j in vertices:
                if dist[make_edge(i, j, directed)] > dist[make_edge(i, k, directed)] + dist[make_edge(k, j, directed)]:
                    dist[make_edge(i, j, directed)] = dist[make_edge(i, k, directed)] + dist[make_edge(k, j, directed)]
    return dist


class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]
        self.cluster_count = n
        self.cluster_size = [1] * (n + 1)

    def find(self, x):
        if self.parent[x] != x:
            return self.find(self.parent[x])
        return x

    def union(self, x, y):
        c1 = self.find(x)
        c2 = self.find(y)
        if c1 == c2:
            return 0
        if self.cluster_size[c1] > self.cluster_size[c2]:
            self.cluster_size[c1] += self.cluster_size[c2]
            self.parent[c2] = c1
        else:
            self.cluster_size[c2] += self.cluster_size[c1]
            self.parent[c1] = c2
        self.cluster_count -= 1
        return 1
##############################################################################