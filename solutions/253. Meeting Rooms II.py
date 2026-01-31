Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.



Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
Example 2:

Input: intervals = [[7,10],[2,4]]
Output: 1


Constraints:

1 <= intervals.length <= 104
0 <= starti < endi <= 106

# Solution

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = [i[0] for i in intervals]
        start.sort()
        end = [i[1] for i in intervals]
        end.sort()
        j = 0
        usedrooms = 0

        for s in range(len(start)):
            if start[s] < end[j]:
                # print("start[s]", start[s])
                # print("end[j]", end[j])
                usedrooms += 1
                # print("usedrooms", usedrooms)
            else:
                j += 1
        return usedrooms