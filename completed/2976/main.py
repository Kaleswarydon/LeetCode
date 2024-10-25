from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


def make_edge_list(src_list, dest_list, weight_list):
    assert len(src_list) == len(dest_list) == len(weight_list)
    return [[src_list[i], dest_list[i], weight_list[i]] for i in range(len(src_list))]


def make_edge(a, b, directed: bool=False):
    return (a, b) if directed else frozenset({a, b})


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


class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        edges = make_edge_list(original, changed, cost)
        dist = floyd_warshall(edges, True)
        res = 0
        for i in range(len(source)):
            res += dist[make_edge(source[i], target[i], True)]
        if res == float("inf"):
            return -1
        return res

if __name__ == '__main__':
    sol = Solution()
    input1 = "abcd", "acbe", ["a","b","c","c","e","d"], ["b","c","b","e","b","e"], [2,5,5,1,2,20]  # 28
    input2 = "aaaa", "bbbb", ["a","c"], ["c","b"], [1,2]  # 12
    input3 = "abcd", "abce", ["a"], ["e"], [10000]  # -1
    print(sol.minimumCost(*input1))
    print(sol.minimumCost(*input2))
    print(sol.minimumCost(*input3))
