class Solution:
    def maxScore(self, s: str) -> int:
        zeros = s.count("0")
        maax, ones = 0, 0
        for i in range(len(s)-1, 0, -1):
            if s[i] == "0":
                zeros -= 1
            if s[i] == "1":
                ones += 1
            maax = max(maax, zeros+ones)
        return maax