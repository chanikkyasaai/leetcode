class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m+n-1
        j = m-1
        k = n-1
        
        while j >= 0 and k >=0:
            if nums1[j] < nums2[k]:
                nums1[i] = nums2[k]
                k-=1
            else:
                nums1[i] = nums1[j]
                j-=1
            i-=1
        
        while k>=0:
            nums1[i] = nums2[k]
            i-=1
            k-=1
        
        return

        