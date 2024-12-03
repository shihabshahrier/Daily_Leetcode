class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res_st = ""
        prev = 0
        for i in spaces:
            res_st += s[prev:i] + " "
            prev = i
        res_st += s[prev:len(s)]
        return res_st
    
# we can also solve it with 
# two pointer
# copy characters in an array -> len(s) + len(spaces)
# and add the spaces according to the spaces