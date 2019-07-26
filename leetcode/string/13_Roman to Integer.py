class Solution:
    def romanToInt(self, s: str) -> int:
        encodeTable = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        total = 0
        if not s:
            return total
        i = len(s) - 1
        while i >= 0:
            if encodeTable[s[i]] > encodeTable[s[i-1]] and i >= 1:
                total += encodeTable[s[i]] - encodeTable[s[i-1]]
                i -= 2
            else:
                total += encodeTable[s[i]]
                i -= 1
        return total
s = Solution()
print(s.romanToInt("MCMXCIV"))
