class Solution:
    def intToRoman(self, num: int) -> str:
        t = [['M', 1000], ['D', 500], ['C', 100], ['L', 50], ['X', 10], ['V', 5], ['I', 1]]
        res = ''
        
        for i in range(0,len(t),2):
            count = num // t[i][1]
            num = num % t[i][1]   

            if count >= 5:  
                if count == 9:
                    res = res + t[i][0] + t[i-2][0] 
                else:
                    res = res + t[i-1][0] + t[i][0]*(count-5)
            else:
                if count == 4:
                    res = res + t[i][0] + t[i-1][0]
                else:
                    res = res + t[i][0]*count
        return res
s = Solution()
