class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []
        curr = 1
        
        for _ in range(n):
            result.append(curr)
            
            if curr * 10 <= n:
                # Move to the next level by multiplying by 10
                curr *= 10
            else:
                # Increment the current number
                if curr >= n:
                    curr //= 10
                curr += 1
                
                # Ensure we don't skip numbers that end with 9
                while curr % 10 == 0:
                    curr //= 10

        return result