class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        max = 0

        l = 0
        
        window = set()
        

        for right in range(len(s)):
            while s[right] in window and l < right:
                window.remove(s[l])
                l += 1
                
            window.add(s[right])
            if len(window) > max:
                max = len(window)

        return max
            





        