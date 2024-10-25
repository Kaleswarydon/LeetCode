from icecream import ic as print
from collections import defaultdict

class Solution:
    def dummy(self, arr, k):
        h = defaultdict(lambda: 0)
        for x in arr:
            h[x] += 1
        res = sorted(h.values(), reverse=True)
        print(res)
        while res and k - res[-1] >= 0:
            k -= res[-1]
            res.pop()
        return len(res)

if __name__ == '__main__':
    sol = Solution()
    input1 = [5,5,4], 1
    input2 = [4,3,1,1,3,3,2], 3
    input3 = [1], 1
    print(sol.dummy(*input1))
    print(sol.dummy(*input2))
    print(sol.dummy(*input3))
