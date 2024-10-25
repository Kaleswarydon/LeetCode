from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import TreeNode
from aux_func.Trie import Trie
from typing import List


class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        d = defaultdict(lambda: [])
        pq = []
        final_vertex_scores = defaultdict(lambda: 0)
        for r in roads:
            d[r[0]].append(r[1])
            d[r[1]].append(r[0])
        for key in d:
            heapq.heappush(pq, (-(len(d[key])), key))
        while pq:
            _, s = heapq.heappop(pq)
            final_vertex_scores[s] = n
            n -= 1
        res = 0
        for r in roads:
            res += final_vertex_scores[r[0]] + final_vertex_scores[r[1]]
        return res


if __name__ == '__main__':
    sol = Solution()
    input1 = 5, [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]
    input2 = 5, [[0,3],[2,4],[1,3]]
    input3 = 5, [[0,1],[1,2],[2,3],[0,3],[4,0]]
    input4 = 9, [[3,8],[8,2],[2,7],[1,6],[6,2],[3,2],[2,5],[5,7],[0,6],[2,4],[4,5],[5,3]]
    print(sol.maximumImportance(*input1))
    print(sol.maximumImportance(*input2))
    print(sol.maximumImportance(*input3))
    print(sol.maximumImportance(*input4))
