from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def go_right(self, coords: tuple, current_dir: chr = 'u'):
        if current_dir == 'u':  # new dir: r
            return [(coords[0], coords[1] + 1), 'r']
        if current_dir == 'd':  # new dir: l
            return [(coords[0], coords[1] - 1), 'l']
        if current_dir == 'l':  # new dir: u
            return [(coords[0] - 1, coords[1]), 'u']
        if current_dir == 'r':  # new dir: d
            return [(coords[0] + 1, coords[1]), 'd']


    def go_straight(self, coords: tuple, current_dir: chr = 'u'):
        if current_dir == 'u':
            return [(coords[0] - 1, coords[1]), 'u']
        if current_dir == 'd':
            return [(coords[0] + 1, coords[1]), 'd']
        if current_dir == 'l':
            return [(coords[0], coords[1] - 1), 'l']
        if current_dir == 'r':
            return [(coords[0], coords[1] + 1), 'r']


    def out_of_bounds(self, cell, dims):
        tmp = [c > dims[i] or c < 0 for i, c in enumerate(cell)]
        #print(cell, dims, tmp, 0 > cell[0] > dims[0])
        return any(tmp)

    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        dims = (rows - 1, cols - 1)
        visited = {}
        res = []
        current_cell = [(rStart, cStart), 'u']
        while len(visited) < rows * cols:
            if not self.out_of_bounds(current_cell[0], dims) and not visited.get(current_cell[0]):
                res.append(list(current_cell[0]))
                visited[current_cell[0]] = True
            old_cell = current_cell
            current_cell = self.go_right(*current_cell)
            if visited.get(current_cell[0]):
                current_cell = self.go_straight(*old_cell)
        return res

if __name__ == '__main__':
    sol = Solution()
    input1 = 1, 4, 0, 0  # [[0,0],[0,1],[0,2],[0,3]]
    input2 = 5, 6, 1, 4  # [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]
    print(sol.spiralMatrixIII(*input1))
    print(sol.spiralMatrixIII(*input2))
