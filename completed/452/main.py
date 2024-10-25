from icecream import ic as print
from collections import defaultdict
import heapq

class Solution:
    def dummy(self, points):
        if not points:
            return 0
        if len(points) == 1:
            return 1
        res = 0
        points.sort(key=lambda x: x[1])
        prev = points[0][1]
        for i in range(1, len(points)):
            if prev >= points[i][0]:
                res += 1
            else:
                prev = points[i][1]
        return len(points) - res

if __name__ == '__main__':
    sol = Solution()
    input1 = [[10,16],[2,8],[1,6],[7,12]] #2
    input2 = [[1,2],[3,4],[5,6],[7,8]] #4
    input3 = [[1,2],[2,3],[3,4],[4,5]] #2
    print(sol.dummy(input1))
    print(sol.dummy(input2))
    print(sol.dummy(input3))
