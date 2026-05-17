class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False 
            
        letters = {}

        for i in s:
            letters[i] = letters.get(i, 0) + 1;
        
        for i in t:
            if i not in letters:
                return False
            letters[i] -= 1
            if letters[i] < 0:
                return False

        
        return True
            

        