class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        lsl = 1
        sw = set(s[0])
        left = 0
        
        for right in range(1,len(s)):
            while s[right] in sw:
                sw.remove(s[left])
                left+=1
                
            sw.add(s[right])
            lsl = max(lsl, right-left+1)
        return lsl
            