from dis import disco

from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Graph:
    def __init__(self):
        self.vertices = defaultdict(list)
    def populate_graph(self, edges):
        for i, (e_s, e_e, w) in enumerate(edges):
            self.vertices[e_s].append([e_e, w])
            self.vertices[e_e].append([e_s, w])
    def __repr__(self):
        return "Graph(\nV=" + str(self.vertices) + ")"

class Solution:
    def dijkstra(self, n, g: Graph, src: int, dst: int):
        dist = [float("inf") for _ in range(n)]
        dist[src] = 0
        tmp_path = []
        pq = [(0, src, None)]
        while pq:
            curr_dist, curr_vertex, prev_vertex = heapq.heappop(pq)
            tmp_path.append(prev_vertex)
            if curr_dist <= dist[curr_vertex]:
                for neigh_vertex, neigh_dist in g.vertices[curr_vertex]:
                    if curr_dist + neigh_dist < dist[neigh_vertex]:
                        dist[neigh_vertex] = curr_dist + neigh_dist
                        heapq.heappush(pq, (dist[neigh_vertex], neigh_vertex, curr_vertex))
        tmp_path.append(dst)
        path = []
        for i in range(len(tmp_path) - 1, 0, -1):
            s, d = tmp_path[i-1], tmp_path[i]
            path.append((s, d))
            if s == src:
                break
        return dist[dst], path[::-1]


    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        def modify_modifyable_edges(start, val):
            for k in range(start, len(edges)):
                if edges[k][2] == -1:
                    edges[k][2] = val
        g = Graph()
        for i, (e_s, e_e, w) in enumerate(edges):
            if w != -1:
                g.vertices[e_s].append([e_e, w])
                g.vertices[e_e].append([e_s, w])
        dij_without_modifiable_edges = self.dijkstra(n, g, source, destination)
        if dij_without_modifiable_edges[0] < target:
            return []
        if dij_without_modifiable_edges[0] == target:
            modify_modifyable_edges(0, 2 * (10 ** 9))
            return edges
        for i, (e_s, e_e, w) in enumerate(edges):
            if w == -1:
                g.vertices[e_s].append([e_e, 1])
                g.vertices[e_e].append([e_s, 1])
                edges[i][2] = 1
                dij_with_modifiable_edges = self.dijkstra(n, g, source, destination)
                if dij_with_modifiable_edges[0] <= target:
                    edges[i][2] += target - dij_with_modifiable_edges[0]
                    modify_modifyable_edges(i + 1, 2 * (10 ** 9))
                    return edges
        return []

if __name__ == '__main__':
    sol = Solution()
    input1 = 5, [[4,1,-1],[2,0,-1],[0,3,-1],[4,3,-1]], 0, 1, 5  # [[4,1,1],[2,0,1],[0,3,3],[4,3,1]]
    input2 = 3, [[0,1,-1],[0,2,5]], 0, 2, 6  # []
    input3 = 4, [[1,0,4],[1,2,3],[2,3,5],[0,3,-1]], 0, 2, 6  # [[1,0,4],[1,2,3],[2,3,5],[0,3,1]]
    print(sol.modifiedGraphEdges(*input1))
    print(sol.modifiedGraphEdges(*input2))
    print(sol.modifiedGraphEdges(*input3))
