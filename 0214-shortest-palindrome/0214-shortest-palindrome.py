class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # Reverse the string s
        rev_s = s[::-1]
        
        # Create a new string by concatenating s, a special character, and the reversed string
        new_s = s + "#" + rev_s
        
        # Compute the KMP table (LPS array)
        n = len(new_s)
        lps = [0] * n  # Longest prefix which is also a suffix
        
        for i in range(1, n):
            j = lps[i - 1]
            
            # Adjust j to find the matching prefix
            while j > 0 and new_s[i] != new_s[j]:
                j = lps[j - 1]
            
            if new_s[i] == new_s[j]:
                j += 1
            
            lps[i] = j
        
        # The length of the longest palindromic prefix in the original string
        longest_palindromic_prefix_length = lps[-1]
        
        # Add the necessary characters in front to make the whole string a palindrome
        to_add = rev_s[:len(s) - longest_palindromic_prefix_length]
        return to_add + s