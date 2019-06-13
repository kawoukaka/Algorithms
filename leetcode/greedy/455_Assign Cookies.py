class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        ans = 0
        j = 0
        for c in g:
            while(j < len(s) and s[j] < c):
                j += 1
            if j < len(s):
                ans += 1
                j += 1
        return ans