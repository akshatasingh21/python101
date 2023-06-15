class Solution:
    def minimumSum(self, num: int) -> int:
        arr = []
        q = num
        r = 0

        while q>0:
            r = q%10
            q = q//10
            arr.append(r)
        
        arr.sort()

        new1 = (arr[0]*10) + arr[2]
        new2 = (arr[1]*10) + arr[3]



        print(new1,new2)
        return new1+new2
