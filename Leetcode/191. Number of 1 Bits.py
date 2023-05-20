class Solution:
    def hammingWeight(self, n: int) -> int:
        a = self.intToBin(n)
        ans = 0
        for i in range(len(a)):
            if a[i] == "1":
                ans = ans + 1
        return ans

    def intToBin(self, n: int) -> str:
        a = n
        ans = ""
        while a > 0:
            r = a % 2
            a = a//2
            ans = ans + str(r)
        return ans[::-1]