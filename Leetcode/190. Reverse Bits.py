class Solution:
    def reverseBits(self, n: int) -> int:
        a = self.intToBin(n)
        a = a[::-1]
        for i in range(len(a),32):
            a = a + "0"
        ans = self.binToInt(a)
        return ans
    
    # Convert Integer to Binary String
    def intToBin(self, a: int) -> str:
        x = a
        ans = ""
        while x > 0:
            y = x%2
            x = x//2
            ans = ans + str(y)
        return ans[::-1]

    
    # Convert Binary String to Integer
    def binToInt(self, b: str) -> int:
        x = b[::-1]
        ans = 0
        pow2 = self.power2(32)
        for i in range(len(x)):
            ans = ans + (pow2[i] * int(x[i]))
        return ans

    # Returns a list of powers of 2 of size n
    def power2(self, n: int) -> [int]:
        ans = [1]
        for i in range(1,n):
            ans.append(ans[i-1]*2)
        return ans