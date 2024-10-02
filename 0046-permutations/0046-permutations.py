class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ln = len(nums)
        self.ans = []
        self.perm(nums,[], [])

        return self.ans

    def perm(self,nums,num, done):
        if len(num) == self.ln:
                self.ans.append(num.copy())
                return

        for i in nums:
            if i not in done:
                num.append(i)
                done.append(i)
                self.perm(nums,num,done)
                num.remove(i)
                done.remove(i)