class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedStr = []

        for i in strs:
            char_list = list(i)
            char_list.sort()
            sorted_string = ''.join(char_list)
            sortedStr.append(sorted_string)
        
        keydict = {}
        j = 0
        for i in sortedStr:
            if i in keydict.keys():
                keydict[i] += [j]
            else:
                keydict[i] =[j]
            j+=1

        ans = []

        for i in keydict.keys():
            lcans = []
            for j in keydict[i] :
                if j <len(strs):
                    lcans.append(strs[j])
            ans.append(lcans)
        
        return ans
        
