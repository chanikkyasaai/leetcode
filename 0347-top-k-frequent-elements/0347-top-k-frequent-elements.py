class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # freq = defaultdict(int)
        # for i  in nums:
        #     freq[i]+=1
        
        # lst = list(map(list, freq.items()))
        # print(lst)
        # sorted_data = sorted(lst, key=lambda x:x[1], reverse=True)
        # sorted_data = sorted_data[:k]
        # print(sorted_data)
        # res = []
        # for i,j in sorted_data:
        #     res.append(i)
        # print(res)
        # return res

        # freq = {}
        # for i in nums:
        #     freq[i] = 1+ freq.get(i,0)

        # freq = Counter(nums)
        # heap = []
        # for num in freq.keys():
        #     heapq.heappush(heap, (freq[num],num))
        #     if len(heap) > k:
        #         heapq.heappop(heap)
        # res = []
        # for i in range(k):
        #     res.append(heapq.heappop(heap)[1])
        # return res

        freq = Counter(nums)
        count = [[] for i in range(len(nums)+1)]
        for num, frq in freq.items():
            count[frq].append(num)
        
        res = []
        for i in range(len(count)-1,0,-1):
            res.extend(count[i])
            if len(res)>= k:
                break
        return res
            