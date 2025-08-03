class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        if not fruits:
            return 0
        
        n = len(fruits)
        
        max_fruits = 0
        left = 0
        current_sum = 0
        
        # Sliding window approach
        for right in range(n):
            current_sum += fruits[right][1]  # Add current fruit count
            
            # Shrink window while steps exceed k
            while left <= right:
                left_pos = fruits[left][0]
                right_pos = fruits[right][0]
                
                # Calculate minimum steps needed for this range
                if startPos < left_pos:
                    steps_needed = right_pos - startPos
                elif startPos > right_pos:
                    steps_needed = startPos - left_pos
                else:
                    # startPos is within range
                    steps_needed = min(startPos - left_pos, right_pos - startPos) + (right_pos - left_pos)
                
                if steps_needed <= k:
                    break
                
                # Remove leftmost element
                current_sum -= fruits[left][1]
                left += 1
            
            if left <= right:
                max_fruits = max(max_fruits, current_sum)
        
        return max_fruits