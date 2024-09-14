class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        op_list = [intervals[0]]
        prev = 0

        for i in range(1,len(intervals)):
            if op_list[prev][1] >= intervals[i][0]:
                if op_list[prev][1] <= intervals[i][1]:
                    op_list[prev][1] = intervals[i][1]
            else:
                op_list.append(intervals[i])
                prev+=1
        
        return op_list
    