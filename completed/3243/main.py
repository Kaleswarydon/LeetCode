from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        def bfs(start, stop):
            q = deque([start])
            visited = defaultdict(lambda: len(g))
            visited[start] = 0
            while q:
                curr = q.popleft()
                for c in g[curr]:
                    if visited[c] > visited[curr] + 1:
                        visited[c] = visited[curr] + 1
                        q.append(c)
            return visited[stop]
        g = defaultdict(list)
        for i in range(1, n):
            g[i-1].append(i)
        res = []
        for q1, q2 in queries:
            g[q1].append(q2)
            res.append(bfs(0, n - 1))
        return res

if __name__ == '__main__':
    sol = Solution()
    input1 = 5, [[2,4],[0,2],[0,4]]  # [3,2,1]
    input2 = 4, [[0,3],[0,2]]  # [1,1]
    input3 = 14, [[0,6],[4,12]]  # [8,6]
    print(sol.shortestDistanceAfterQueries(*input1))
    print(sol.shortestDistanceAfterQueries(*input2))
    print(sol.shortestDistanceAfterQueries(*input3))
