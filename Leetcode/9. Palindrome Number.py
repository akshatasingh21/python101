class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = str(x)
        if y == y[::-1]:
            return True
        return False


class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = x
        d = 0
        while y > 0:
            r = y%10
            y = y//10
            #print ("{} & {}".format(r,y))

            d = d*10 + r
            #print("{} & {}".format(r,d))
        
        if d == x:
            return True

        return False


class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = x
        d = 0
        while y > 0:
            d = d * 10
            d = d + y%10
            y = y//10

        return d == x

