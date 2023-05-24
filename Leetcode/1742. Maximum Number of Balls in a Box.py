class Solution:
    def sumDigits(self, num: int) -> int:
        x = num
        sum = 0

        while x > 0:
            sum = sum + (x%10)
            x = x//10

        return sum

    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        n = highLimit - lowLimit +1
        m = {}

        for i in range(lowLimit,highLimit+1,1):
            sm = self.sumDigits(i)
            
            if sm in m:
                m[sm]= m[sm] + 1
            else:
                m[sm] = 1

        a = 0
        for i in m.keys():
            if m[i] > a:
                a = m[i]

        print(a)
        return a
