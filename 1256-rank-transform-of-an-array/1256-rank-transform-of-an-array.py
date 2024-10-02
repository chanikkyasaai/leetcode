class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # if len(arr) == 0:
        #     return []

        # sortedarr = sorted(arr)
        # rankdict = {}
        # i=0

        # for  j in range(len(arr)):
        #     if sortedarr[j] in rankdict:
        #         continue
        #     i+=1
        #     rankdict[sortedarr[j]] = i

        # for j in range(len(arr)):
        #     arr[j] = rankdict[arr[j]]

        # return arr

        sortedarr = sorted(set(arr))
        rankdict = {ele : rank+1 for rank,ele in enumerate(sortedarr)}
        ranklist = [rankdict[ele] for ele in arr]

        return ranklist
        
            
