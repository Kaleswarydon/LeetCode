#from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
#from aux_func.Trie import Trie
from typing import List


null = None


class TrieNode:
    def __init__(self, value="_ROOT_"):
        self.value: str = value
        self.children: List[TrieNode] = []
        self.visited: int = 0
        self.is_complete: bool = False

    def contains(self, item):
        for x in self.children:
            if x.value == item:
                return x
        return False

    def __repr__(self):
        return str(self.value + ", " + str(self.visited))

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for c in word:
            current.visited += 1
            tmp = current.contains(c)
            if not tmp:
                tmp = TrieNode(c)
                current.children.append(tmp)
            current = tmp
        current.visited += 1
        current.is_complete = True

    def find(self, word, prefix=False, strict=False, visited_cntr=None):
        '''
        :param word: The word that should be processed
        :param prefix: Indicates if a prefix, whether it's a valid word or not, is a valid result
        :param smallest_prefix: Indicates if the smallest existing prefix of word in the tree should be returned
        :param strict: Indicates if a prefix has to be a valid word on its own
        :param visited_cntr: string, options: simple, cumulative: specifies if node.visited should be returned, cumulative if all visited values (incl prefixes)
        :return: empty string if not found, prefix/word if found AND visited count (simple/cumulative) if specified
        '''

        def ret(r, c1, c2):
            if visited_cntr == "simple":
                return r, c1
            elif visited_cntr == "cumulative":
                return r, c2
            else:
                return r, -1

        current = self.root
        res = ""
        cumulative_visited = 0
        for c in word:
            tmp = current.contains(c)
            if not tmp:
                return ret("", 0, cumulative_visited)
            current = tmp
            res += current.value
            cumulative_visited += current.visited
            if strict and current.is_complete:
                if prefix:
                    return ret(res, current.visited, cumulative_visited)
        if prefix or current.is_complete:
            return ret(res, current.visited, cumulative_visited)
        return ret("", 0, cumulative_visited)

    def __print_trie__(self):
        def helper(node: TrieNode, level=0):
            for _ in range(level):
                print('\t', end='')
            print(node)
            for c in node.children:
                helper(c, level+1)
        return helper(self.root)

    def __repr__(self):
        print("")
        self.__print_trie__()
        return ""

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        t = Trie()
        for w1 in words:
            t.insert(w1)
        res = [0] * len(words)
        for i, w2 in enumerate(words):
            _, amount = t.find(w2, prefix=True, visited_cntr="cumulative")
            res[i] += amount
        return res

if __name__ == '__main__':
    sol = Solution()
    input1 = ["abc","ab","bc","b"]  # [5,4,3,2]
    input2 = ["abcd"]  # [4]
    print(sol.sumPrefixScores(input1))
    print(sol.sumPrefixScores(input2))
