from icecream import ic as print
from collections import defaultdict
import heapq

class Solution:
    def dummy(self, tasks, n):
        if tasks:
            pq = [(0, tasks[0])]
            ht = defaultdict(lambda: 0)
            ht[tasks[0]] = n + 1
        else:
            return 0
        for i in range(1, len(tasks)):
            heapq.heappush(pq, (ht[tasks[i]], tasks[i]))
            ht[tasks[i]] += n + 1
        #res = []
        cntr = 0
        j = 0
        while pq:
            if pq[0][0] <= j:
                item = heapq.heappop(pq)
                #res.append(item)
            else:
                pass
                #res.append((j, 'idle'))
            cntr += 1
            j += 1
        #return len(res)
        return cntr

def print_res(res):
    for i, x in enumerate(res):
        __builtins__.print(f'{x[1]}', end='')
        if not i == len(res) - 1:
            __builtins__.print(f'->', end='')
    print('\n')

if __name__ == '__main__':
    sol = Solution()
    input1 = ["A","A","A","B","B","B"], 2
    input2 = ["A","C","A","B","D","B"], 1
    input3 = ["A","A","A","B","B","B"], 3
    print(sol.dummy(*input1))
    print(sol.dummy(*input2))
    print(sol.dummy(*input3))
