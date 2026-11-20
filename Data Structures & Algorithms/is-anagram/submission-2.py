class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        while len(s) != 0 and len(t) !=0:
            sChar = [char for char in s]
            tChar = [char for char in t]
            if len(sChar) != len(tChar):
                return False
            elif sorted(sChar) != sorted(tChar):
                return False 
            return True