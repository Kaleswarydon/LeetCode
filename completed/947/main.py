from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]
        self.cluster_count = n
        self.cluster_size = [1] * (n + 1)

    def __repr__(self):
        return "UnionFind(\nParents: " + str(self.parent) + ",\nClusterCount:" + str(self.cluster_count) + "\n)"

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
    def removeStones(self, stones: List[List[int]]) -> int:
        uf = UnionFind(len(stones))
        stones.sort(key=lambda x: x[0])
        col_start_ind = stones[-1][0] + 1
        cluster_d = defaultdict(list)
        res = 0
        for i, s in enumerate(stones):
            cluster_d[s[0]].append(i)
            cluster_d[col_start_ind + s[1]].append(i)
        for cl in cluster_d.values():
            for j in range(1, len(cl)):
                res += uf.union(cl[0], cl[j])
        return res




if __name__ == '__main__':
    sol = Solution()
    input1 = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]  # 5
    input2 = [[0,0],[0,2],[1,1],[2,0],[2,2]]  # 3
    input3 = [[0,0]]  # 0
    input4 = [[1,2],[0,1],[7,3],[5,5],[7,1],[6,1],[0,6],[5,1],[4,2],[8,4]]  # 7
    print(sol.removeStones(input1))
    print(sol.removeStones(input2))
    print(sol.removeStones(input3))
    print(sol.removeStones(input4))
