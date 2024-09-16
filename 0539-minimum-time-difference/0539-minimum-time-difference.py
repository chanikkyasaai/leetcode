class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        
        minutes = []
        for time in timePoints:
            h,m = map(int, time.split(':'))
            minutes.append(h*60 + m)
        
        minutes.sort()

        min_difference = float('inf')

        for i in range(1,len(minutes)):
            min_difference = min(min_difference, minutes[i]- minutes[i-1])
        
        wrap_arround_diff = 1440 - (minutes[-1] - minutes[0])
        min_difference = min(min_difference, wrap_arround_diff)
        return min_difference