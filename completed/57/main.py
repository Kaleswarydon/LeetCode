from icecream import ic as print
from collections import defaultdict
import heapq

class Solution:
    def dummy(self, intervals, newInterval):
        if not intervals:
            return [newInterval]
        if not newInterval:
            return intervals
        tmp = []
        for i, interval in enumerate(intervals):
            if interval[0] <= newInterval[0] <= interval[1] or interval[0] <= newInterval[1] <= interval[1] or (newInterval[0] <= interval[0] and newInterval[1] >= interval[1]):
                tmp.append(i)
        if tmp:
            mi = intervals[min(tmp)][0]
            ma = intervals[max(tmp)][1]
            merged_interval = [min(mi, newInterval[0]), max(ma, newInterval[1])]
            intervals[tmp.pop()] = merged_interval
            if tmp:
                for t in tmp[::-1]:
                    del intervals[t]
        else:
            intervals.append(newInterval)
            intervals.sort()
        return intervals

if __name__ == '__main__':
    sol = Solution()
    input1 = [[1,3],[6,9]], [2,5]
    input2 = [[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]
    input3= [[1,5]], [6,8]
    print(sol.dummy(*input1))
    print(sol.dummy(*input2))
    print(sol.dummy(*input3))
