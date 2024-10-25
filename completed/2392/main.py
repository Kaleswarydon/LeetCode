from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def topological_order(self, g: dict, k: int) -> List[int] | None:
        n = k
        in_deg = [0 for _ in range(n+1)]
        for adj in g:
            for dest in g[adj]:
                in_deg[dest] += 1
        q = deque()
        for i in range(1, len(in_deg)):
            if not in_deg[i]:
                q.append(i)
        ind = 0
        order = [0 for _ in range(n)]
        while q:
            at = q.pop()
            order[ind] = at
            ind += 1
            for dest in g[at]:
                in_deg[dest] -= 1
                if not in_deg[dest]:
                    q.append(dest)
        if ind != n:
            return None
        return order

    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        m = [[0 for x in range(k)] for y in range(k)]
        g1 = defaultdict(lambda: set())
        _ = [g1[x].add(y) for x, y in rowConditions]
        g2 = defaultdict(lambda: set())
        _ = [g2[x].add(y) for x, y in colConditions]
        o1 = self.topological_order(g1, k)
        if not o1:
            return []
        o2 = self.topological_order(g2, k)
        if not o2:
            return []
        for r in range(k):
            for c in range(k):
                if o1[r] == o2[c]:
                    m[r][c] = o1[r]
        return m

if __name__ == '__main__':
    sol = Solution()
    input1 = 3, [[1,2],[3,2]], [[2,1],[3,2]]  # [[3,0,0],[0,0,1],[0,2,0]]
    input2 = 3, [[1,2],[2,3],[3,1],[2,3]], [[2,1]]  # []
    print(sol.buildMatrix(*input1))
    print(sol.buildMatrix(*input2))
