class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        m = {}
        cnt = 0
        for i in range(len(jewels)):
            m[jewels[i]] = True
        
        print(m)

        for i in range(len(stones)):
            if stones[i] in m:
                cnt = cnt + 1


        return cnt
