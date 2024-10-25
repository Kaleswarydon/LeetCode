from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        start_v = 1
        dest_v = n
        g = defaultdict(lambda: [])
        for v1, v2 in edges:
            g[v1].append(v2)
            g[v2].append(v1)
        q = deque([start_v])
        visited_v = defaultdict(lambda: [])
        curr_t = 0
        dest_v_visited = False
        while q:
            for _ in range(len(q)):
                curr_v = q.popleft()
                if curr_v == dest_v:
                    if dest_v_visited:
                        return curr_t
                    dest_v_visited = True
                for neighbor_v in g[curr_v]:
                    if curr_t not in visited_v[neighbor_v] and len(visited_v[neighbor_v]) < 2:
                        q.append(neighbor_v)
                        visited_v[neighbor_v].append(curr_t)
            div_t, mod_t = divmod(curr_t, change)
            curr_t += time + (change - mod_t if div_t % 2 else 0)

if __name__ == '__main__':
    sol = Solution()
    input1 = 5, [[1,2],[1,3],[1,4],[3,4],[4,5]], 3, 5  # 13
    input2 = 2, [[1,2]], 3, 2  # 11
    input3 = 6, [[1,2],[1,3],[2,4],[3,5],[5,4],[4,6]], 3, 100
    print(sol.secondMinimum(*input1))
    print(sol.secondMinimum(*input2))
    print(sol.secondMinimum(*input3))
