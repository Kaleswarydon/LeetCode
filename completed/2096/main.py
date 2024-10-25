from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def get_parent_dict(self, root): # simple bfs
        res = defaultdict(lambda: ('X', -1))
        q = deque([root])
        while q:
            item = q.popleft()
            if item:
                if item.left:
                    res[item.left.val] = ('L', item.val)
                if item.right:
                    res[item.right.val] = ('R', item.val)
                q.append(item.left)
                q.append(item.right)
        return res

    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def backtrack(pd, value):
            path_directions = []
            path_values = [value]
            while True:
                direction, value = pd[value]
                path_directions.append(direction)
                path_values.append(value)
                if direction == 'X':
                    break
            path_directions.append('X')
            return path_directions, path_values
        parent_dict = self.get_parent_dict(root)
        path_to_start_directions, path_to_start_values = backtrack(parent_dict, startValue)
        path_to_dest_directions, path_to_dest_values = backtrack(parent_dict, destValue)
        cut = len(set(path_to_start_values).intersection(path_to_dest_values))
        path_to_start_directions = path_to_start_directions[:-cut]
        path_to_dest_directions = path_to_dest_directions[:-cut]
        return ''.join(['U' for x in path_to_start_directions if x]) + ''.join(reversed(path_to_dest_directions))


if __name__ == '__main__':
    sol = Solution()
    input1 = bfs_list_to_binary_tree([5,1,2,3,null,6,4]), 3, 6  # "UURL"
    input2 = bfs_list_to_binary_tree([2,1]), 2, 1  # "L"
    input3 = bfs_list_to_binary_tree([5,8,3,1,null,4,7,6,null,null,null,null,null,null,2]), 5, 6  # "LLL"
    input4 = bfs_list_to_binary_tree([1,null,10,12,13,4,6,null,15,null,null,5,11,null,2,14,7,null,8,null,null,null,9,3]), 6, 15  # "UURR"
    input5 = bfs_list_to_binary_tree([3,6,5,null,null,13,8,9,19,11,2,10,17,null,null,null,18,null,14,null,null,null,null,15,null,4,16,null,null,null,null,null,7,null,1,12]), 10, 13  # "UU"
    input6 = bfs_list_to_binary_tree([13,5,4,7,null,8,6,3,null,null,12,9,1,null,null,11,null,null,10,null,null,null,null,2]), 3, 2  # "UUURRLRL"
    print(sol.getDirections(*input1))
    print(sol.getDirections(*input2))
    print(sol.getDirections(*input3))
    print(sol.getDirections(*input4))
    print(sol.getDirections(*input5))
    print(sol.getDirections(*input6))
