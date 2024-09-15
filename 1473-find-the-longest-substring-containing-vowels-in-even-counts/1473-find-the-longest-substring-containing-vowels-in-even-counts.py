class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        # Map to store the first occurrence of each bitmask
        vowel_mask_map = {0: -1}  # Initial mask 0 at index -1
        vowels = 'aeiou'
        bitmask = 0
        max_len = 0
        
        for i, char in enumerate(s):
            # Update the bitmask if the current character is a vowel
            if char in vowels:
                # Find the position of the vowel in 'aeiou'
                vowel_index = vowels.index(char)
                # Toggle the corresponding bit
                bitmask ^= (1 << vowel_index)
            
            # Check if the bitmask has been seen before
            if bitmask in vowel_mask_map:
                # Calculate the length of the substring
                max_len = max(max_len, i - vowel_mask_map[bitmask])
            else:
                # Store the first occurrence of this bitmask
                vowel_mask_map[bitmask] = i
        
        return max_len