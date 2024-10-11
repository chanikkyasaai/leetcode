class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        n = len(times)
        
        # Add friend index to times for identification
        times_with_index = [(times[i][0], times[i][1], i) for i in range(n)]
        
        # Sort by arrival time
        times_with_index.sort()
        
        # Min-heap for available chairs
        available_chairs = list(range(n))
        heapq.heapify(available_chairs)
        
        # Min-heap to track when a chair will be freed: (leave time, chair number)
        leaving_heap = []
        
        for arrival, leaving, friend_index in times_with_index:
            # Free all chairs of friends who left before or at current arrival time
            while leaving_heap and leaving_heap[0][0] <= arrival:
                leave_time, chair = heapq.heappop(leaving_heap)
                heapq.heappush(available_chairs, chair)
            
            # Assign the smallest available chair to the current friend
            chair_assigned = heapq.heappop(available_chairs)
            
            # If this is the target friend, return the chair number
            if friend_index == targetFriend:
                return chair_assigned
            
            # Push the friend's leaving time and chair back into the leaving heap
            heapq.heappush(leaving_heap, (leaving, chair_assigned))

        return -1  # In case something goes wrong (shouldn't happen)