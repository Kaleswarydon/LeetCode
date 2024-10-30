from icecream import ic as print
from collections import defaultdict, deque
import heapq
from aux_func.LinkedList import *
from aux_func.Tree import *
from aux_func.Trie import Trie
from typing import List


null = None


class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        def rec(curr_row, curr_col, prev):
            if curr_row < 0 or curr_row == len(grid) or curr_col == len(grid[0]) or prev >= grid[curr_row][curr_col]:
                return 0
            if memo[(curr_row, curr_col)] != -1:
                return memo[(curr_row, curr_col)]
            a = rec(curr_row - 1, curr_col + 1, grid[curr_row][curr_col])
            b = rec(curr_row, curr_col + 1, grid[curr_row][curr_col])
            c = rec(curr_row + 1, curr_col + 1, grid[curr_row][curr_col])
            memo[(curr_row, curr_col)] = 1 + max(a,b,c)
            return memo[(curr_row, curr_col)]
        memo = defaultdict(lambda: -1)
        for i in range(len(grid)):
            rec(i, 0, -2)
        return max(memo.values()) - 1




if __name__ == '__main__':
    sol = Solution()
    input1 = [[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]  # 3
    input2 = [[3,2,4],[2,1,9],[1,1,7]]  # 0
    input3 = [[1000000,92910,1021,1022,1023,1024,1025,1026,1027,1028,1029,1030,1031,1032,1033,1034,1035,1036,1037,1038,1039,1040,1041,1042,1043,1044,1045,1046,1047,1048,1049,1050,1051,1052,1053,1054,1055,1056,1057,1058,1059,1060,1061,1062,1063,1064,1065,1066,1067,1068], [1069,1070,1071,1072,1073,1074,1075,1076,1077,1078,1079,1080,1081,1082,1083,1084,1085,1086,1087,1088,1089,1090,1091,1092,1093,1094,1095,1096,1097,1098,1099,1100,1101,1102,1103,1104,1105,1106,1107,1108,1109,1110,1111,1112,1113,1114,1115,1116,1117,1118]]
    print(sol.maxMoves(input1))
    print(sol.maxMoves(input2))
    print(sol.maxMoves(input3))

