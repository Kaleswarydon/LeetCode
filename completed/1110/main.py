from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def get_connections(self, root): # simple bfs
        parents = defaultdict(lambda: ('X', TreeNode(-1)))
        children = defaultdict(lambda: [None, None])
        q = deque([root])
        while q:
            item = q.popleft()
            if item:
                children[item] = [None, None]
                if item.left:
                    parents[item.left.val] = ('L', item)
                    children[item.val][0] = item.left
                if item.right:
                    parents[item.right.val] = ('R', item)
                    children[item.val][1] = item.right
                q.append(item.left)
                q.append(item.right)
        return parents, children

    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        new_roots = []
        if root.val not in to_delete:
            new_roots.append(root)
        parent_dict, children_dict = self.get_connections(root)
        for d in to_delete:
            direction, parent = parent_dict[d]
            print(direction, parent)
            if direction == 'L':
                parent.left = None
            else:
                parent.right = None
            for x in children_dict[d]:
                if x and x.val not in to_delete:
                    new_roots.append(x)
        new_roots = [nr for nr in new_roots if nr]
        return new_roots

if __name__ == '__main__':
    sol = Solution()
    input1 = bfs_list_to_binary_tree([1,2,3,4,5,6,7]), [3,5]  # [[1,2,null,4],[6],[7]]
    input2 = bfs_list_to_binary_tree([1,2,4,null,3]), [3]  # [[1,2,4]]
    input3 = bfs_list_to_binary_tree([1,2,null,4,3]), [2,3]  # [[1],[4]]
    input4 = bfs_list_to_binary_tree([1,2,3,null,null,null,4]), [2,1]  #
    #print(sol.delNodes(*input1))
    #print(sol.delNodes(*input2))
    #print(sol.delNodes(*input3))
    print(sol.delNodes(*input4))
