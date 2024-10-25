class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        input = list(s)
        stack = []
        for i, x in enumerate(input):
            if stack and x == ")" and stack[-1][1] == "(":
                stack.pop()
            else:
                stack.append([i, x])
        for x in stack:
            input[x[0]] = "x"
        res = max([len(x) for x in ''.join(input).split("x")])
        return res


if __name__ == '__main__':
    sol = Solution()
    s0 = "(()"  # 2
    s1 = ")()())"  # 4
    s2 = "()(()"  # 2
    s3 = "(()())"  # 6
    s4 = "()()"  # 4
    s5 = "()(())"  # 6
    s6 = "()((())"  # 4
    print(s0, sol.longestValidParentheses(s0))
    print()
    print(s1, sol.longestValidParentheses(s1))
    print()
    print(s2, sol.longestValidParentheses(s2))
    print()
    print(s3, sol.longestValidParentheses(s3))
    print()
    print(s4, sol.longestValidParentheses(s4))
    print()
    print(s5, sol.longestValidParentheses(s5))
    print()
    print(s6, sol.longestValidParentheses(s6))
