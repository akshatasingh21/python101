class Solution:
    def gcd(self, x: int, y: int) -> int:
        num = 0
        if x > y:
            num = y
        else:
            num = x

        fac = 1
        for i in range(2,num+1,1):
            if (y%i == 0 and x%i == 0):
                fac = i
                return fac
        return fac
        

    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        m = {}
        
        for i in range(len(deck)):
            if deck[i] in m:
                m[deck[i]] = m[deck[i]] + 1
            else:
                m[deck[i]] = 1
        
        val = []
        for i in m.keys():
            if m[i] != 1:
                val.append(m[i])
            else:
                return False

        val.sort()
        print(val)

        gcd = 1
        if len(val) > 1:
            gcd = self.gcd(val[0], val[1])
            print(gcd)
            if gcd == 1:
                return False
        else:
            gcd = self.gcd(val[0], val[0])
            print(gcd)
            if gcd == 1:
                return False

        for i in range(len(val)):
            if val[i]%gcd == 0:
                continue
            else:
                return False
                break
           
        return True
