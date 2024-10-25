from icecream import ic as print
#from heapq import heappop, heappush, heapify
import heapq
import time

class Solution:
    def dummy(self, n, meetings):
        free_rooms = list(range(n))
        full_rooms = []
        freq = [0] * n
        meetings.sort()
        free_room = heapq.heappop(free_rooms)
        heapq.heappush(full_rooms, (meetings[0][1], free_room))
        freq[free_room] += 1
        for i in range(1, len(meetings)):
            while full_rooms and full_rooms[0][0] <= meetings[i][0]:
                heapq.heappush(free_rooms, heapq.heappop(full_rooms)[1])
            if len(full_rooms) < n:
                free_room = heapq.heappop(free_rooms)
                heapq.heappush(full_rooms, (meetings[i][1], free_room))
            else:
                end_time, free_room = heapq.heappop(full_rooms)
                heapq.heappush(full_rooms, (end_time + meetings[i][1] - meetings[i][0], free_room))
            freq[free_room] += 1
        freq_max = freq.index(max(freq))
        return freq_max

if __name__ == '__main__':
    start_time = time.time_ns()
    sol = Solution()
    input1 = 2, [[0, 10], [1, 5], [2, 7], [3, 4]]
    input2 = 3, [[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]]
    input3 = 3, [[0, 10], [1, 9], [2, 8], [3, 7], [4, 6]]
    input4 = 4, [[18,19],[3,12],[17,19],[2,13],[7,10]]
    #print(sol.dummy(*input1))
    #print(sol.dummy(*input2))
    #print(sol.dummy(*input3))
    print(sol.dummy(*input4))

    print("time:", (time.time_ns() - start_time) / 1000000000)