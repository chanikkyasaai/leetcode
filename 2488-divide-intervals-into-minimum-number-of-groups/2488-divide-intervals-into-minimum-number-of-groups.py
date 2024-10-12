class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        pq = []
        l = 0
        for left, right in sorted(intervals):
            if pq and pq[0] < left:
                heappop(pq)
                l-=1
            heappush(pq, right)
            l+=1
        return l
            