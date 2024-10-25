from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.res = 0
        def dfs(node):
            if not node:
                return []
            if not node.left and not node.right:
                return [0]
            left_dists = dfs(node.left)
            right_dists = dfs(node.right)
            for l in left_dists:
                for r in right_dists:
                    if l + r + 2 <= distance:
                        self.res += 1
            return list(map(lambda x: x + 1, left_dists + right_dists))
        dfs(root)
        return self.res


if __name__ == '__main__':
    sol = Solution()
    input1 = bfs_list_to_binary_tree([1,2,3,null,4]), 3  # 1
    input2 = bfs_list_to_binary_tree([1,2,3,4,5,6,7]), 3  # 2
    input3 = bfs_list_to_binary_tree([7,1,4,6,null,5,3,null,null,null,null,null,2]), 3  # 1
    input4 = bfs_list_to_binary_tree([1,1,1]), 2  # 1
    input5 = bfs_list_to_binary_tree([100]), 1  # 0
    input6 = bfs_list_to_binary_tree([11,99,88,77,null,null,66,55,null,null,44,33,null,null,22]), 1  # 0
    input7 = bfs_list_to_binary_tree([80,null,3,95,28,null,null,null,28]), 1  # 1
    input8 = bfs_list_to_binary_tree([59,11,44,13,46,57,88,59,25]), 1  #
    input9 = bfs_list_to_binary_tree([19,10,64,75,5,68,64,53,35,63,53,76,45,48,6,13,31,8,72,10,79,9,96,45,null,null,63,7,65,null,7,35,74,null,null,56,null,70,41,null,null,64,null,null,null,null,null,null,null,86,97,null,null,null,null,null,null,53,67,null,null,98,null,null,null,null,null,null,null,null,null,34,null,null,null,64,null,62]), 1  # 0
    input10 = bfs_list_to_binary_tree([15, 66, 55, 97, 60, 12, 56, null, 54, null, 49, null, 9, null, null, null, null, null, 90]), 5  # 3
    input11 = bfs_list_to_binary_tree([80,62,99,36,45,39,76,81,44,23,58,8,14,1,94,100,10,8,30,75,7,33,80,44,2,67,78,64,30,98,100,24,48,42,31,91,37,81,45,30,77,28]), 8  # 122
    print(sol.countPairs(*input1))
    print(sol.countPairs(*input2))
    print(sol.countPairs(*input3))
    print(sol.countPairs(*input4))
    print(sol.countPairs(*input5))
    print(sol.countPairs(*input6))
    print(sol.countPairs(*input7))
    print(sol.countPairs(*input8))
    print(sol.countPairs(*input9))
    print(sol.countPairs(*input10))
    print(sol.countPairs(*input11))
