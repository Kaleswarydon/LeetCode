from icecream import ic as print

class Solution:
    def dummy(self, s):
        if len(s) < 2:
            return len(s)
        pointer_low = 0
        pointer_high = len(s) - 1
        current_char = s[pointer_low]
        while pointer_low < pointer_high and s[pointer_low] == s[pointer_high]:
            while pointer_low < len(s) - 1 and s[pointer_low] == current_char:
                pointer_low += 1
            while pointer_high >= 0 and s[pointer_high] == current_char:
                pointer_high -= 1
            current_char = s[pointer_low]
        return len(s[pointer_low:pointer_high + 1])

if __name__ == '__main__':
    sol = Solution()
    input1 = "cabaabac"
    input2 = "aabccabba"
    input3 = "c"
    input4 = "bbbbbbbbbbbbbbbbbbb"
    print(sol.dummy(input1))
    print(sol.dummy(input2))
    print(sol.dummy(input3))
    print(sol.dummy(input4))
