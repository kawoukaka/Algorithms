class Solution:
    def addDigits(self, num: int) -> int:
        while num / 10 >= 1:
            num = str(num)
            temp = 0
            for digit in num:
                temp += int(digit)
                num = temp

        return num
        