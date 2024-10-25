from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def go_right(self, coords: tuple):
        current_dir = coords[2]
        if current_dir == 'u':  # new dir: r
            return coords[0], coords[1] + 1, 'r'
        if current_dir == 'd':  # new dir: l
            return coords[0], coords[1] - 1, 'l'
        if current_dir == 'l':  # new dir: u
            return coords[0] - 1, coords[1], 'u'
        if current_dir == 'r':  # new dir: d
            return coords[0] + 1, coords[1], 'd'

    def go_straight(self, coords: tuple):
        current_dir = coords[2]
        if current_dir == 'u':
            return coords[0] - 1, coords[1], 'u'
        if current_dir == 'd':
            return coords[0] + 1, coords[1], 'd'
        if current_dir == 'l':
            return coords[0], coords[1] - 1, 'l'
        if current_dir == 'r':
            return coords[0], coords[1] + 1, 'r'

    def out_of_bounds(self, cell: tuple, dims: tuple):
        tmp = [c > dims[i] or c < 0 for i, c in enumerate(cell)]
        # print(cell, dims, tmp, 0 > cell[0] > dims[0])
        return any(tmp)

    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        dims = (m - 1, n - 1)
        res = [[-1 for _ in range(n)] for _ in range(m)]
        current_node = head
        current_cell = (0, 0, "r")
        while current_node:
            res[current_cell[0]][current_cell[1]] = current_node.val
            tmp_next_cell = self.go_straight(current_cell)
            if self.out_of_bounds(tmp_next_cell[:2], dims) or res[tmp_next_cell[0]][tmp_next_cell[1]] != -1:
                current_cell = self.go_right(current_cell)
            else:
                current_cell = tmp_next_cell
            current_node = current_node.next
        return res


if __name__ == '__main__':
    sol = Solution()
    input1 = 3, 5, make_linked_list([3,0,2,6,8,1,7,9,4,2,5,5,0])  # [[3,0,2,6,8],[5,0,-1,-1,1],[5,2,4,9,7]]
    input2 = 1, 4, make_linked_list([0,1,2])  # [[0,1,2,-1]]
    print(sol.spiralMatrix(*input1))
    print(sol.spiralMatrix(*input2))
