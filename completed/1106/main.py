from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def op_func(self, op: chr, ex: list) -> chr:
        #print(op, ex)
        while len(ex) > 1:
            a = ex.pop()
            b = ex.pop()
            if op == '&':
                ex.append(a and b)
            elif op == '|':
                ex.append(a or b)
        if op == '!':
            ex[0] = not ex[0]
        tmp = ex.pop()
        return 't' if tmp else 'f'

    def parseBoolExpr(self, expression: str) -> bool:
        res = []
        for c in expression:
            #print(c)
            if c == ',' or c == '(':
                continue
            if c == ')':
                #print(res[-1])
                tmp = []
                while res[-1] not in ['&', '|', '!']:
                    v = res.pop()
                    tmp.append(True if v == 't' else False)
                res.append(self.op_func(res.pop(), tmp))
            else:
                res.append(c)
            #print(res)
        tmp = res.pop()
        return True if tmp == 't' else False

if __name__ == '__main__':
    sol = Solution()
    input1 = "&(|(f))"  # False
    input2 = "|(f,f,f,t)"  # True
    input3 = "!(&(f,t))"  # True
    input4 = "|(&(t,f,t),!(t))"  # False
    input5 = "|(f,&(t,t))"  # True
    print(sol.parseBoolExpr(input1))
    print(sol.parseBoolExpr(input2))
    print(sol.parseBoolExpr(input3))
    print(sol.parseBoolExpr(input4))
    print(sol.parseBoolExpr(input5))
