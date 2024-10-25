from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import TreeNode
from typing import List


class Node:
    def __init__(self, value=""):
        self.value: str = value
        self.children: List[Node] = []
        self.is_complete: bool = False

    def contains(self, item):
        for x in self.children:
            if x.value == item:
                return x
        return False

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        current = self.root
        for c in word:
            tmp = current.contains(c)
            if not tmp:
                tmp = Node(c)
                current.children.append(tmp)
            current = tmp
        current.is_complete = True

    def find(self, word, prefix=False, strict=False):
        '''
        :param word: The word that should be processed
        :param prefix: Indicates if a prefix, whether it's a valid word or not, is a valid result
        :param strict: Indicates if a prefix has to be a valid word on its own
        :return: empty string if not found, prefix/word if found
        '''
        current = self.root
        res = ""
        for c in word:
            tmp = current.contains(c)
            if not tmp:
                return ""
            current = tmp
            res += current.value
            if strict and current.is_complete:
                if prefix:
                    return res
        if prefix or current.is_complete:
            return res
        return ""

    def search(self, word):
        return self.find(word, prefix=False, strict=True)

    def startsWith(self, word, strict=False):
        return self.find(word, prefix=True, strict=strict)


class Solution:
    def dummy(self):
        #["insert","search","search","search","startsWith","startsWith","startsWith"]
        t = Trie()
        t.insert("hello")
        print(t.search("hell"))
        print(t.search("helloa"))
        print(t.search("hello"))
        print(t.startsWith("hell"))
        print(t.startsWith("helloa"))
        print(t.startsWith("hello"))



if __name__ == '__main__':
    sol = Solution()
    input1 = ["hello", "hell", "helloa", "hello", "hell", "helloa", "hello"]

    print(sol.dummy())
