from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func import Tree
from aux_func.Tree import TreeNode
from aux_func.Trie import Trie
from typing import List


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        node_dict = defaultdict(lambda: TreeNode())
        for node_val, node_child_val, node_child_direction_left in descriptions:
            if not node_dict[node_val].val:
                node_dict[node_val].val = node_val
            if not node_dict[node_child_val].val:
                node_dict[node_child_val].val = node_child_val
            if node_child_direction_left:
                node_dict[node_val].left = node_dict[node_child_val]
            else:
                node_dict[node_val].right = node_dict[node_child_val]
        node_has_parent_set = set(node_dict.keys())
        for k in node_dict.keys():
            for c in [node_dict[k].left, node_dict[k].right]:
                try:
                    node_has_parent_set.remove(c.val)
                except:
                    continue
        return node_dict[node_has_parent_set.pop()]




if __name__ == '__main__':
    sol = Solution()
    input1 = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]  # [50,20,80,15,17,19]
    input2 = [[1,2,1],[2,3,0],[3,4,1]]  # [1,2,null,null,3,4]
    print(Tree.binary_tree_to_bfs_list(sol.createBinaryTree(input1)))
    print(Tree.binary_tree_to_bfs_list(sol.createBinaryTree(input2)))
