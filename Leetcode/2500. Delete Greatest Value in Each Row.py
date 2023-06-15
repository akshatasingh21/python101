class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        arr = []

        for i in range(len(grid)):
            arr = grid[i]
            arr.sort()
            grid[i] = arr
        
        ans = 0
        
        for i in range(len(grid[0])):
            cnt = len(grid)
            m = 0
            arr2 = []
            while cnt > 0 :
                arr2.append(grid[m][i])
                m = m+1
                cnt = cnt - 1
            print(arr2)

            arr2.sort()
            ans = ans + arr2[-1]


        print(ans)
        return ans
    
# Solution 2
class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        arr = []

        for i in range(len(grid)):
            grid[i].sort()
        
        ans = 0
        
        for i in range(len(grid[0])):
            x = grid[0][i]
            for j in range(len(grid)):
                if x < grid[j][i]:
                    x = grid[j][i]

            ans = ans + x


        print(ans)
        return ans