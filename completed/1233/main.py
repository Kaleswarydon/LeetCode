from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort(reverse=True)
        res = []
        while folder:
            curr = folder.pop()
            res.append(curr)
            tmp = []
            while folder and not folder[-1].find(curr):
                t = folder.pop()
                if len(t) > len(curr) and t[len(curr)] != '/':
                    tmp.append(t)
            folder.extend(tmp[::-1])
        return res


if __name__ == '__main__':
    sol = Solution()
    input1 = ["/a","/a/b","/c/d","/c/d/e","/c/f"]  # ["/a","/c/d","/c/f"]
    input2 = ["/a/b/c","/a/b/d","/a"]  # ["/a"]
    input3 = ["/a/b/c","/a/b/ca","/a/b/d"]  # ["/a/b/c","/a/b/ca","/a/b/d"]
    input4 = ["/ab","/abc","/abd"]  # ["/ab","/abc","/abd"]
    print(sol.removeSubfolders(input1))
    print(sol.removeSubfolders(input2))
    print(sol.removeSubfolders(input3))
    print(sol.removeSubfolders(input4))
