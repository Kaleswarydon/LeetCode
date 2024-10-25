from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def bfs(root: Optional[TreeNode], mode: str = "add"):
            '''
            :param root: TreeNode
            :param mode: "add" or "del"
            :return: True if went through, False if it didnt find a counterpart to delete (in "del" mode)
            '''
            q = deque([(root, -1)])
            while q:
                node, parent_val = q.popleft()
                if not node:
                    continue
                if mode == "add":
                    tmp.add((node.val, parent_val))
                else:
                    try:
                        tmp.remove((node.val, parent_val))
                    except KeyError:
                        return False
                if node.left:
                    q.append((node.left, node.val))
                if node.right:
                    q.append((node.right, node.val))
            return True
        tmp = set()
        a = bfs(root1, "add")
        b = bfs(root2, "del")
        return a and b and not len(tmp)

if __name__ == '__main__':
    sol = Solution()
    input1 = bfs_list_to_binary_tree([1,2,3,4,5,6,null,null,null,7,8]), bfs_list_to_binary_tree([1,3,2,null,6,4,5,null,null,null,null,8,7])  # True
    input2 = bfs_list_to_binary_tree([]), bfs_list_to_binary_tree([]) # True
    input3 = bfs_list_to_binary_tree([]), bfs_list_to_binary_tree([1]) # False
    print(sol.flipEquiv(*input1))
    print(sol.flipEquiv(*input2))
    print(sol.flipEquiv(*input3))
