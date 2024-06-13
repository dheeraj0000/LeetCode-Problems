class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c_s = ""
        max_length = 0
        for char in s:
            if char in c_s:
                c_s = c_s[c_s.index(char) + 1:]
            c_s += char
            max_length = max(max_length, len(c_s))
        
        return max_length
