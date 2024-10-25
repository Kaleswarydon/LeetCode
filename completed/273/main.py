from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def num_to_triplet_str_list(self, n: int) -> List[str]:
        num_str = str(n)[::-1]
        while len(num_str) % 3:
            num_str += '0'
        nums = [num_str[i:i + 3] for i in range(0, len(num_str), 3)]
        return nums[::-1]


    def convert_triplet_to_words(self, triplet: str):
        prefix = ["Zero", "One", "Tw", "Th", "Fo", "Fi", "Six", "Seven", "Eigh", "Nin", "Ten", "Eleven", "Twelve"]
        default = ["", "", "o", "ree", "ur", "ve", "", "", "t", "e", ""]
        tens = ["", "teen", "enty", "irty", "rty", "fty", "ty", "ty", "ty", "ety"]
        res = deque()
        if triplet == "000":
            return "Zero"
        for i, digit in enumerate(triplet):
            digit_int = int(digit)
            if prefix[digit_int] == "Zero":
                continue
            if i == 2:  # hundreds
                res.append("Hundred")
                res.append(default[digit_int])
            elif i:  # tens
                res.append(tens[digit_int])
            else:  # ones
                res.append(default[digit_int])
            res.append(prefix[digit_int])
        res.reverse()
        res_str = ''.join(res)
        res_str = res_str.replace("OneteenNine", "Nineteen")
        res_str = res_str.replace("OneteenEight", "Eighteen")
        res_str = res_str.replace("OneteenSeven", "Seventeen")
        res_str = res_str.replace("OneteenSix", "Sixteen")
        res_str = res_str.replace("OneteenFive", "Fifteen")
        res_str = res_str.replace("OneteenFour", "Fourteen")
        res_str = res_str.replace("OneteenThree", "Thirteen")
        res_str = res_str.replace("OneteenTwo", "Twelve")
        res_str = res_str.replace("OneteenOne", "Eleven")
        res_str = res_str.replace("Oneteen", "Ten")
        return res_str


    def numberToWords(self, num: int) -> str:
        magnitude = ["", "Thousand", "Million", "Billion"]
        tmp = deque()
        nums = self.num_to_triplet_str_list(num)
        for i, triplet in enumerate(nums[::-1]):
            triplet_words = self.convert_triplet_to_words(triplet)
            if "Zero" not in triplet_words:
                tmp.append(magnitude[i])
            tmp.append(triplet_words)
        tmp.reverse()
        tmp_str = ''.join(tmp)
        res_str = ""
        for j, c in enumerate(tmp_str):
            if c.isupper() and j:
                res_str += ' '
            res_str += c
        if len(res_str) > 4:
            res_str = res_str.replace("Zero", "").strip()
        res_str = ' '.join(res_str.split())
        return res_str



if __name__ == '__main__':
    sol = Solution()
    input1 = 123  # "One Hundred Twenty Three"
    input2 = 12345  # "Twelve Thousand Three Hundred Forty Five"
    input3 = 1234567  # "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
    input4 = 111
    input5 = 110
    input6 = 0
    input7 = 1
    input8 = 113
    input9 = 180
    input10 = 1000
    input11 = 1000000
    input12 = 1000010
    print(sol.numberToWords(input1))
    print(sol.numberToWords(input2))
    print(sol.numberToWords(input3))
    print(sol.numberToWords(input4))
    print(sol.numberToWords(input5))
    print(sol.numberToWords(input6))
    print(sol.numberToWords(input7))
    print(sol.numberToWords(input8))
    print(sol.numberToWords(input10))
    print(sol.numberToWords(input11))
    print(sol.numberToWords(input12))
