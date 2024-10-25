from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List

null = None


class Solution:

    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def is_3x3_magic_square(x: int, y: int) -> int:
            #all existing 3x3 magic squares, hardcoded
            magic_squares = [816357492, 618753294, 276951438, 438951276, 294753618, 492357816, 834159672, 672159834]
            square_as_int = 0
            cntr = 0
            for i in range(3):
                for j in range(3):
                    square_as_int += grid[x+i-1][y+j-1] * (10 ** cntr)
                    cntr += 1
            return int(square_as_int in magic_squares)
        if len(grid) < 3 or len(grid[0]) < 3:
            return 0
        res = 0
        for k in range(1, len(grid) - 1):
            for l in range(1, len(grid[0]) - 1):
                res += is_3x3_magic_square(k, l)
        return res


if __name__ == '__main__':
    sol = Solution()
    input1 = [[4, 3, 8, 4], [9, 5, 1, 9], [2, 7, 6, 2]]  # 1
    input2 = [[8]]  # 0
    input3 = [[1, 2], [3, 4]]  # 0
    input4 = [[5, 5, 5], [5, 5, 5], [5, 5, 5]]  # 0
    input5 = [[4,7,8],[9,5,1],[2,3,6]]  # 0
    print(sol.numMagicSquaresInside(input1))
    print(sol.numMagicSquaresInside(input2))
    print(sol.numMagicSquaresInside(input3))
    print(sol.numMagicSquaresInside(input4))
    print(sol.numMagicSquaresInside(input5))
