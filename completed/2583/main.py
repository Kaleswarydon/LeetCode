from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        r = defaultdict(int)
        q = deque([(root, 0)])
        while q:
            item, depth = q.popleft()
            if item:
                r[depth] += item.val
                q.append((item.left, depth + 1))
                q.append((item.right, depth + 1))
        if k - 1 >= len(r.values()):
            return -1
        return sorted(r.values(), reverse=True)[k-1]


if __name__ == '__main__':
    sol = Solution()
    input1 = bfs_list_to_binary_tree([5,8,9,2,1,3,7,4,6]), 2  # 13
    input2 = bfs_list_to_binary_tree([1,2,null,3]), 1  # 3
    print(sol.kthLargestLevelSum(*input1))
    print(sol.kthLargestLevelSum(*input2))
