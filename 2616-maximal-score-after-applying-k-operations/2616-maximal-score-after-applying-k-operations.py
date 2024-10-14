class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        score = 0
        max_heap = []
        for i  in nums:
            heapq.heappush(max_heap, -i)
        
        for i in range(k):
            x = heapq.heappop(max_heap)
            score+= x
            x= math.ceil(-x/3)
            heapq.heappush(max_heap,-x)
        
        return -score