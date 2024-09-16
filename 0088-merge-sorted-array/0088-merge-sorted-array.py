import math

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    #     for i in range(m, m+n):
    #         nums1[i] = nums2[i-m]

    #     nums1 = self.quicksort(nums1, 0, len(nums1)-1)

    # def partition(self, arr, lb, ub):
    #     pivot = arr[lb]
    #     start = lb
    #     end = ub

    #     while start< end:

    #         while start <= ub and arr[start] <= pivot:
    #             start+=1
    #         while arr[end] > pivot:
    #             end -=1
    #         if start < end:
    #             arr[start], arr[end] = arr[end], arr[start]

    #     arr[lb], arr[end] = arr[end], arr[lb]
    #     return end

    
    # def quicksort(self, arr, lb,  ub):
    #     if lb < ub:
    #         loc = self.partition(arr, lb, ub)
    #         self.quicksort(arr, lb, loc-1)
    #         self.quicksort(arr, loc+1, ub)

    #     return arr

        for i in range(m, m+n):
            nums1[i] = nums2[i-m]

        # applying gap method

        gap = math.ceil((m+n)/2)

        while gap >=1 :
            left = 0
            right = left + gap

            while left < m+n and right < m+n:
                if nums1[left] > nums1[right]:
                    nums1[left], nums1[right] = nums1[right], nums1[left]
                left +=1
                right+=1
            
            if gap == 1:
                break
            gap = math.ceil(gap / 2)