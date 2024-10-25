from icecream import ic as print
from collections import defaultdict
import heapq

class Solution:
    def dummy(self, order, s):
        d = defaultdict(lambda: len(order))
        pq = []
        for i, o in enumerate(order):
            d[o] = i
        for x in s:
            heapq.heappush(pq, (d[x], x))
        res = ""
        while True:
            try:
                res += heapq.heappop(pq)[1]
            except IndexError:
                break
        return res

if __name__ == '__main__':
    sol = Solution()
    input1 = "cba", "abcd"
    print(sol.dummy(*input1))
