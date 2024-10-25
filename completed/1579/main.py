from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import TreeNode
from aux_func.Trie import Trie
from typing import List


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

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice = UnionFind(n)
        bob = UnionFind(n)
        edge_cntr = 0
        pq = [[-i, j, k] for i, j, k in edges]
        heapq.heapify(pq)
        while pq:
            tmp_cntr = 0
            edge_type, src, dest = heapq.heappop(pq)
            if edge_type == -1 or edge_type == -3:
                if alice.union(src, dest):
                    tmp_cntr = 1
            if edge_type == -2 or edge_type == -3:
                if bob.union(src, dest):
                    tmp_cntr = 1
            edge_cntr += tmp_cntr
        if not (alice.cluster_count == 1 and bob.cluster_count == 1):
            return -1
        return len(edges) - edge_cntr

if __name__ == '__main__':
    sol = Solution()
    input1 = 4, [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]  # 2
    input2 = 4, [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]  # 0
    input3 = 4, [[3,2,3],[1,1,2],[2,3,4]]  # -1
    input4 = 4, [[3,1,2],[3,3,4]]  # -1
    input5 = 13, [[1,1,2],[2,1,3],[3,2,4],[3,2,5],[1,2,6],[3,6,7],[3,7,8],[3,6,9],[3,4,10],[2,3,11],[1,5,12],[3,3,13],[2,1,10],[2,6,11],[3,5,13],[1,9,12],[1,6,8],[3,6,13],[2,1,4],[1,1,13],[2,9,10],[2,1,6],[2,10,13],[2,2,9],[3,4,12],[2,4,7],[1,1,10],[1,3,7],[1,7,11],[3,3,12],[2,4,8],[3,8,9],[1,9,13],[2,4,10],[1,6,9],[3,10,13],[1,7,10],[1,1,11],[2,4,9],[3,5,11],[3,2,6],[2,1,5],[2,5,11],[2,1,7],[2,3,8],[2,8,9],[3,4,13],[3,3,8],[3,3,11],[2,9,11],[3,1,8],[2,1,8],[3,8,13],[2,10,11],[3,1,5],[1,10,11],[1,7,12],[2,3,5],[3,1,13],[2,4,11],[2,3,9],[2,6,9],[2,1,13],[3,1,12],[2,7,8],[2,5,6],[3,1,9],[1,5,10],[3,2,13],[2,3,6],[2,2,10],[3,4,11],[1,4,13],[3,5,10],[1,4,10],[1,1,8],[3,3,4],[2,4,6],[2,7,11],[2,7,10],[2,3,12],[3,7,11],[3,9,10],[2,11,13],[1,1,12],[2,10,12],[1,7,13],[1,4,11],[2,4,5],[1,3,10],[2,12,13],[3,3,10],[1,6,12],[3,6,10],[1,3,4],[2,7,9],[1,3,11],[2,2,8],[1,2,8],[1,11,13],[1,2,13],[2,2,6],[1,4,6],[1,6,11],[3,1,2],[1,1,3],[2,11,12],[3,2,11],[1,9,10],[2,6,12],[3,1,7],[1,4,9],[1,10,12],[2,6,13],[2,2,12],[2,1,11],[2,5,9],[1,3,8],[1,7,8],[1,2,12],[1,5,11],[2,7,12],[3,1,11],[3,9,12],[3,2,9],[3,10,11]]  # 114
    print(sol.maxNumEdgesToRemove(*input1))
    print(sol.maxNumEdgesToRemove(*input2))
    print(sol.maxNumEdgesToRemove(*input3))
    print(sol.maxNumEdgesToRemove(*input4))
    print(sol.maxNumEdgesToRemove(*input5))
