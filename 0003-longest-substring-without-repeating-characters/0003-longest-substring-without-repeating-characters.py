class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<1:
            return 0
        win = set(s[0])
        lsl = 1
        left=0

        for right in range(1,len(s)):
            while s[right] in win:
                win.remove(s[left])
                left+=1
            win.add(s[right])
            right+=1
            lsl = max(lsl, right-left)

        return lsl