from icecream import ic as print
from collections import defaultdict, deque
import heapq

import aux_func.Tree
from aux_func.LinkedList import *
from aux_func.Tree import TreeNode
from aux_func.Trie import Trie
from typing import List

null = None

class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        def binary_tree_to_bfs_list(root: TreeNode, only_values=False):
            res = []
            q = deque([root])
            while q:
                item = q.popleft()
                if item:
                    res.append(item.val)
                    q.append(item.left)
                    q.append(item.right)
                elif not only_values:
                    res.append(None)
            while res[-1] is None:
                res.pop()
            return res

        def bfs_list_to_binary_tree(l: list, root_only=True):
            current = 0
            current_left_assigned_none = False
            node_list = [TreeNode(val=l[0])]
            for i in range(1, len(l)):
                current_node = node_list[current]
                tmp = None
                while not current_node:
                    current += 1
                    current_node = node_list[current]
                if current_node:
                    if l[i] is not None:
                        tmp = TreeNode(val=l[i])
                    else:
                        tmp = None
                    if current_node.left is None and not current_left_assigned_none:
                        current_node.left = tmp
                        current_left_assigned_none = True
                    elif current_node.right is None:
                        current_node.right = tmp
                        current += 1
                        current_left_assigned_none = False
                node_list.append(tmp)
            if root_only:
                return node_list[0]
            return node_list

        values = sorted(binary_tree_to_bfs_list(root, True), reverse=True)
        prefix_sums = [values[0]]
        for i in range(1, len(values)):
            prefix_sums.append(values[i] + prefix_sums[-1])
        prefix_sum_dict = defaultdict(lambda: 0)
        for k, v in zip(values, prefix_sums):
            prefix_sum_dict[k] = v
        res_list = binary_tree_to_bfs_list(root)
        for i in range(len(res_list)):
            if res_list[i] is not None:
                res_list[i] = prefix_sum_dict.get(res_list[i])
        res = bfs_list_to_binary_tree(res_list, False)
        res = res[0]
        return res

if __name__ == '__main__':
    sol = Solution()
    input1 = aux_func.Tree.bfs_list_to_binary_tree([4, 1, 6, 0, 2, 5, 7, null, null, null, 3, null, null, null, 8])  # [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
    input2 = aux_func.Tree.bfs_list_to_binary_tree([0, null, 1])  # [1,null,1]
    input3 = aux_func.Tree.bfs_list_to_binary_tree([4, 1, 12, 0, 2, 5, 14, null, null, null, 3, null, 10, null, 15, null, null, null, 11])
    print(sol.bstToGst(input1))
    print(sol.bstToGst(input2))
    print(sol.bstToGst(input3))
