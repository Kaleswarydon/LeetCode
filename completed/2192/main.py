from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import TreeNode
from aux_func.Trie import Trie
from typing import List


class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        def get_anc(current_node, adjacency_list, visited_nodes):
            visited_nodes.add(current_node)
            for neighbour in adjacency_list[current_node]:
                if neighbour not in visited_nodes:
                    get_anc(neighbour, adjacency_list, visited_nodes)
        adj_list = [[] for _ in range(n)]
        for edge in edges:
            src, dest = edge
            adj_list[dest].append(src)
        res = []
        for i in range(n):
            anc = []
            visited = set()
            get_anc(i, adj_list, visited)
            anc = list(visited)
            anc.remove(i)
            res.append(sorted(anc))
        return res

if __name__ == '__main__':
    sol = Solution()
    input1 = 8, [[0,3],[0,4],[1,3],[2,4],[2,7],[3,5],[3,6],[3,7],[4,6]]  # [[],[],[],[0,1],[0,2],[0,1,3],[0,1,2,3,4],[0,1,2,3]]
    input2 = 5, [[0,1],[0,2],[0,3],[0,4],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]  # [[],[0],[0,1],[0,1,2],[0,1,2,3]]
    print(sol.getAncestors(*input1))
    print(sol.getAncestors(*input2))
