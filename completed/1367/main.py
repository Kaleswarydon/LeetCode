from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.LinkedList import make_linked_list
from aux_func.Tree import *
from aux_func.Tree import bfs_list_to_binary_tree
from aux_func.Trie import Trie
from typing import List


null = None

def make_linked_list(l: List[int]):
    head = ListNode(l[0])
    current = head
    for x in l[1:]:
        current.next = ListNode(x)
        current = current.next
    return head

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


class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def bt_find_path(root: Optional[TreeNode], p: List[int]):
            path_nodes = deque()
            tmp_q = deque([root])
            while tmp_q:
                item = tmp_q.popleft()
                if item:
                    if item.left:
                        tmp_q.append(item.left)
                    if item.right:
                        tmp_q.append(item.right)
                    if item.val == p[0]:
                        path_nodes.append((item, 1))
            while path_nodes:
                item, ni = path_nodes.popleft()
                if ni == len(p):
                    return True
                if item.left and item.left.val == p[ni]:
                    path_nodes.append((item.left, ni + 1))
                if item.right and item.right.val == p[ni]:
                    path_nodes.append((item.right, ni + 1))
            return False
        ll_as_list = []
        current_ll_node = head
        while current_ll_node:
            ll_as_list.append(current_ll_node.val)
            current_ll_node = current_ll_node.next
        return bt_find_path(root, ll_as_list)

if __name__ == '__main__':
    sol = Solution()
    input1 = make_linked_list([4,2,8]), bfs_list_to_binary_tree([1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3])  # True
    input2 = make_linked_list([1,4,2,6]), bfs_list_to_binary_tree([1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3])  # True
    input3 = make_linked_list([1,4,2,6,8]), bfs_list_to_binary_tree([1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3])  # False
    print(sol.isSubPath(*input1))
    print(sol.isSubPath(*input2))
    print(sol.isSubPath(*input3))
