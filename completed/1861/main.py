from icecream import ic as print
from collections import defaultdict, deque
import heapq

from setuptools.command.rotate import rotate

from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        def rotate(m): #rotate 90deg (clockwise)
            return [[m[j][i] for j in range(len(m) - 1, -1, -1)] for i in range(len(m[0]))]
        def gravity(m):
            for j in range(len(m[0])):
                free_tiles = 0
                for i in range(len(m) -1, -1, -1):
                    match m[i][j]:
                        case '.':
                            free_tiles += 1
                        case '*':
                            free_tiles = 0
                        case '#':
                            m[i][j] = '.'
                            m[i + free_tiles][j] = '#'
                        case _:
                            pass
            return m
        return gravity(rotate(box))


if __name__ == '__main__':
    sol = Solution()
    input1 = [["#",".","#"]]
    input2 = [["#",".","*","."],["#","#","*","."]]
    input3 = [["#","#","*",".","*","."],["#","#","#","*",".","."],["#","#","#",".","#","."]]
    print(sol.rotateTheBox(input1))
    print(sol.rotateTheBox(input2))
    print(sol.rotateTheBox(input3))
