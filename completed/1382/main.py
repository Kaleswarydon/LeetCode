from icecream import ic as print
from collections import defaultdict, deque
import heapq

import aux_func.Tree
from aux_func.LinkedList import *
from aux_func.Tree import TreeNode
from aux_func.Trie import Trie
from typing import List


class Solution:
    def inorder_traversal(self, node: TreeNode):
        def helper(node: TreeNode):
            if node is None:
                return None
            helper(node.left)
            res.append(node.val)
            helper(node.right)
        res = []
        helper(node)
        return res

    def make_balanced_bst_from_inorder_list(self, node_list):  # make balanced bst from inorder list
        def helper(ptr_lo, ptr_hi):
            if ptr_lo > ptr_hi:
                return None
            new_root_index = (ptr_lo + ptr_hi) // 2
            new_root = TreeNode(node_list[new_root_index])
            new_root.left = helper(ptr_lo, new_root_index - 1)
            new_root.right = helper(new_root_index + 1, ptr_hi)
            return new_root
        return helper(0, len(node_list) - 1)

    def balanceBST(self, root: TreeNode) -> TreeNode:
        node_list = sorted(self.inorder_traversal(root))
        return self.make_balanced_bst_from_inorder_list(node_list)


if __name__ == '__main__':
    null = None
    sol = Solution()
    input1 = aux_func.Tree.bfs_list_to_binary_tree([1, null, 2, null, 3, null, 4, null, null])  # [2,1,3,null,null,null,4]
    input2 = aux_func.Tree.bfs_list_to_binary_tree([2, 1, 3])  # [2,1,3]
    print(sol.balanceBST(input1))
    print(sol.balanceBST(input2))
