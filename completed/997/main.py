from icecream import ic as print
from collections import defaultdict


class Solution:
    def dummy(self, n, trust):
        trusts = [0] * (n + 1)
        is_trusted = [0] * (n + 1)
        for t in trust:
            trusts[t[0]] += 1
            is_trusted[t[1]] += 1
        res = [k for k in [i for i, j in enumerate(is_trusted) if j == n - 1] if not trusts[k]]
        if res:
            return res[0]
        else:
            return -1

if __name__ == '__main__':
    sol = Solution()
    input1 = 2, [[1,2]]
    input2 = 3, [[1,3],[2,3]]
    input3 = 3, [[1,3],[2,3],[3,1]]
    print(sol.dummy(*input1))
    print(sol.dummy(*input2))
    print(sol.dummy(*input3))
