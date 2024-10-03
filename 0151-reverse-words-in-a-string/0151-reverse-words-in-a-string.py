class Solution:
    def reverseWords(self, s: str) -> str:
        # words = list(s.split())
        # words = words[::-1]
        # ans = " ".join(words)

        ans = []
        temp = ""
        for i in s:
            if i!= " ":
                temp+=i
            elif temp!= "":
                ans.append(temp)
                temp = ""
        if temp !="":
            ans.append(temp)

        return " ".join(ans[::-1])
