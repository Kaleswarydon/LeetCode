from icecream import ic as print

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(set(s)) != len(set(t)):
            return False
        d = {}
        res = ""
        for i in range(len(s)):
            d.update({s[i]: t[i]})
        for i in range(len(s)):
            res += d.get(s[i])
        return res == t

if __name__ == '__main__':
    sol = Solution()
    s = "babc"
    t = "baba"
    print(sol.isIsomorphic(s, t))