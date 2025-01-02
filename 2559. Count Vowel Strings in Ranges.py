class Solution:
    def possible(self, s):
        v = "aeiou"
        if s[0] in v and s[-1] in v:
            return True
        return False
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        pos = [0]
        for i in range(len(words)):
            if self.possible(words[i]):
                pos.append(pos[i] + 1)
            else:
                pos.append(pos[i])
        ans = []
        for l, r in queries:
            ans.append(pos[r+1]-pos[l])
        return ans