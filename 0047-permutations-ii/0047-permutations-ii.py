class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.count = Counter(nums) 
        self.nums = sorted(nums)
        self.perm([])

        return self.ans

    def perm(self, num):
        if len(num) == len(self.nums):
            self.ans.append(num.copy())
            return
        
        for i in self.count: 
            if self.count[i] > 0: 
                num.append(i)          
                self.count[i] -= 1     
                self.perm(num)        
                num.pop()              
                self.count[i] += 1 