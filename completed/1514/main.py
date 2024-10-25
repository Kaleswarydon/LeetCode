from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List
import math

null = None

class Graph:
    def __init__(self):
        self.vertices = set()
        self.edges = defaultdict(None)
    def populate_graph(self, edges, weights):
        for i, e in enumerate(edges):
            self.vertices.update(e)
            self.edges[frozenset(e)] = weights[i]
    def __repr__(self):
        return "Graph(\nV=" + str(self.vertices) + "\nE=" + str(self.edges) + ")"


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = defaultdict(list)
        for i in range(len(edges)):
            src = edges[i][0]
            dst = edges[i][1]
            adj[src].append((dst, succProb[i]))
            adj[dst].append((src, succProb[i]))
        visited = set()
        pq = [(-1, start_node)]
        while pq:
            prob, curr = heapq.heappop(pq)
            visited.add(curr)
            if curr == end_node:
                return prob * -1
            for n, n_p in adj[curr]:
                if n not in visited:
                    heapq.heappush(pq, (n_p * prob, n))
        return 0

if __name__ == '__main__':
    sol = Solution()
    input1 = 3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.2], 0, 2  # 0.25000
    input2 = 3, [[0,1],[1,2],[0,2]], [0.5,0.5,0.3], 0, 2  # 0.30000
    input3 = 3, [[0,1]], [0.5], 0, 2  # 0.00000
    print(sol.maxProbability(*input1))
    print(sol.maxProbability(*input2))
    print(sol.maxProbability(*input3))
