from copy import deepcopy

from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Tree import bfs_list_to_binary_tree
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        def dfs(r):
            def postorder(n, depth, height):
                if n:
                    if n.left:
                        postorder(n.left, depth + 1, height + 1)
                        lv = n.left.val
                    else:
                        lv = -1
                    if n.right:
                        postorder(n.right, depth + 1, height + 1)
                        rv = n.right.val
                    else:
                        rv = -1
                    if not (n.left or n.right):
                        heights[n.val] = 0
                    else:
                        heights[n.val] = max(heights[lv], heights[rv]) + 1
                    depths[n.val] = depth
            heights = defaultdict(int)
            depths = defaultdict(int)
            postorder(r, 0, float("inf"))
            return heights, depths
        def rem(r_val):
            l = dep[r_val]
            h = hei[r_val]
            #print(l,h,level_maxes)
            if level_maxes[l][0] == h:
                tmp = level_maxes[l][1]
            else:
                tmp = level_maxes[l][0]
            #print(l,tmp,l + tmp)
            return l + tmp
        hei, dep = dfs(root)
        level_maxes = defaultdict(lambda: [-1,-1])
        for d in dep.keys():
            if level_maxes[dep[d]][0] < hei[d]:
                level_maxes[dep[d]][1] = level_maxes[dep[d]][0]
                level_maxes[dep[d]][0] = hei[d]
                continue
            if level_maxes[dep[d]][1] < hei[d]:
                level_maxes[dep[d]][1] = hei[d]
        result = []
        for q in queries:
            result.append(rem(q))
        return result

if __name__ == '__main__':
    sol = Solution()
    input1 = bfs_list_to_binary_tree([1,3,4,2,null,6,5,null,null,null,null,null,7]), [4]  # [2]
    input2 = bfs_list_to_binary_tree([5,8,9,2,1,3,7,4,6]), [3,2,4,8]  # [3,2,3,2]
    input3 = bfs_list_to_binary_tree([1,null,5,3,null,2,4]), [3,5,4,2,4]  # [1,0,3,3,3]
    input4 = bfs_list_to_binary_tree([5,3,9,2,4,8,10,1,null,null,null,6,null,null,null,null,null,null,7]), [4]  # [4]
    print(sol.treeQueries(*input1))
    print(sol.treeQueries(*input2))
    print(sol.treeQueries(*input3))
    print(sol.treeQueries(*input4))
