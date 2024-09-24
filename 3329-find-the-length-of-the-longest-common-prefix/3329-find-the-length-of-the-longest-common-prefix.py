class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        # brute force solution

        # str1 = list(map(str, arr1))
        # str2 = list(map(str, arr2))

        # lcp = 0

        # for i in str1:
        #     for j in str2:
        #         min_length = min(len(i), len(j))
        #         common_length = 0

        #         for n in range(min_length):
        #             if i[n] == j[n]:
        #                 common_length +=1
        #             else:
        #                 break
        #         lcp = max(lcp, common_length)
        
        # return lcp
        
        # optimal

        ans_set = set()

        # str1 = list(map(str, arr1))
        # str2 = list(map(str, arr2))

        lcp = 0

        for i in arr1:
            while i:
                ans_set.add(i)
                i//= 10
        
        for x in arr2:
            while x:
                if x in ans_set:
                    lcp = max(lcp, len(str(x)))
                x//=10

        return lcp