class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # ans = []
        # sum = 0
        # rem_dict = {0:[-1]}

        # for i in range(len(nums)):
        #     sum += nums[i]
        #     rem = sum % k
        #     if rem <0:
        #         rem+= k
        #     if rem in rem_dict:
        #         subarr = []
        #         for start_index in rem_dict[rem]:
        #             subarr = nums[start_index:i+1]
        #             ans.append(subarr)
        #     if rem not in rem_dict:
        #         rem_dict[rem] = []

        #     rem_dict[rem].append(i)

        # return ans

        count = 0
        sum = 0
        rem_dict = {0:1}

        for i in range(len(nums)):
            sum += nums[i]
            rem = sum % k
            if rem <0:
                rem+= k
            if rem in rem_dict:
                count+= rem_dict[rem]
                rem_dict[rem]+=1
            else:
                rem_dict[rem] = 1

        return count








