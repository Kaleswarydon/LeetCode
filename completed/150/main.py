from icecream import ic as print


class Solution:
    def arith_func(self, op):
        if op == '+':
            return lambda a, b: a + b
        if op == '-':
            return lambda a, b: a - b
        if op == '*':
            return lambda a, b: a * b
        if op == '/':
            return lambda a, b: int(a / b)
        raise Exception("invalid")

    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        ops = ['+', '-', '*', '/']
        for t in tokens:
            if t in ops:
                b = int(stack.pop())
                a = int(stack.pop())
                af = self.arith_func(t)
                stack.append(af(a, b))
            else:
                stack.append(t)
        return int(stack[0])


if __name__ == '__main__':
    sol = Solution()
    tokens1 = ["2", "1", "+", "3", "*"]
    tokens2 = ["4", "13", "5", "/", "+"]
    tokens3 = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    tokens4 = ['18']
    print(sol.evalRPN(tokens1))
    print(sol.evalRPN(tokens2))
    print(sol.evalRPN(tokens3))
    print(sol.evalRPN(tokens4))
