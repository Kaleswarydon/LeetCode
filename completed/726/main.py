from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import TreeNode
from aux_func.Trie import Trie
from typing import List


class Solution:
    def prepare_input(self, formula: str) -> List[int]:
        formula_list = []
        for x in formula:
            if x.islower():
                formula_list.append(formula_list.pop() + x)
            else:
                tmp = x
                try:
                    _ = int(x) + int(formula_list[-1])
                    tmp = formula_list.pop() + x
                except:
                    pass
                formula_list.append(tmp)
        return formula_list

    def prepare_output(self, res_dict):
        res = ""
        for x in sorted(res_dict.keys()):
            res += x
            if res_dict[x] != 1:
                res += str(int(res_dict[x]))
        return res

    def is_int(self, s):
        try:
            tmp = int(s)
        except:
            tmp = None
        return tmp


    def countOfAtoms(self, formula: str) -> str:
        print(formula)
        res_dict = defaultdict(lambda: 0)
        formula_list = self.prepare_input(formula)
        multi_list = []
        current_multi = 1
        one_time_multi = 1
        for x in formula_list[::-1]:
            if (t := self.is_int(x)) is not None:
                one_time_multi = t
                continue
            if x == ')':
                multi_list.append(one_time_multi)
                current_multi *= one_time_multi
            elif x != '(':
                res_dict[x] += one_time_multi * current_multi
            else:
                current_multi //= multi_list.pop()
            one_time_multi = 1
        return self.prepare_output(res_dict)


if __name__ == '__main__':
    sol = Solution()
    input1 = "H2O"  # "H2O"
    input2 = "Mg(OH)2"  # "H2MgO2"
    input3 = "K4(ON(SO3)2)2"  # "K4N2O14S4"
    input4 = "C6H12O6"
    input5 = "Be32"
    input6 = "H50"
    print(sol.countOfAtoms(input1))
    print(sol.countOfAtoms(input2))
    print(sol.countOfAtoms(input3))
    print(sol.countOfAtoms(input4))
    print(sol.countOfAtoms(input5))
    print(sol.countOfAtoms(input6))
