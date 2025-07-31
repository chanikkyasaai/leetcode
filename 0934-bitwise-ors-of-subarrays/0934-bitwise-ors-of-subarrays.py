class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        # res = set()
        # n = len(arr)

        # for i in range(n):
        #     or_val = 0
        #     for j in range(i, n):
        #         or_val |= arr[j]
        #         res.add(or_val)

        # return len(res)
        res = set()
        cur = set()

        for num in arr:
            new_curr ={num}
            for prev in cur:
                new_curr.add(prev | num)
            
            cur = new_curr
            res.update(cur)

        return len(res)
