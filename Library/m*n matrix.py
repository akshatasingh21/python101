def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20]]
        ans = []

        # print list row-wise
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                ans.append(arr[i][j])

        # print list column-wise
        for i in range(len(arr[0])):
            for j in range(len(arr)):
                ans.append(arr[j][i])
        
        # Diagonal1 elements
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                if i == j:
                    ans.append(arr[i][j]) 
        
        # Diagonal2 elements
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                if i + j == len(arr[i]) - 1:
                    ans.append(arr[i][j])
        
        # Diagonal3 elements
        for i in range(len(arr[0])):
            for j in range(len(arr)):
                if i + j == len(arr[i]) - 1:
                    ans.append(arr[j][i])
        
        # Diagonal4 elements
        for i in range(len(arr)-1,-1,-1):
            for j in range(len(arr[i])-1,-1,-1):
                if i == j:
                    ans.append(arr[i][j])
        
        # Tircha elements
        sum = (len(arr) - 1) + (len(arr[0]) - 1)
        for i in range(0,sum+1):
            for j in range(0,len(arr[0])):
                for k in range(0,len(arr)):
                    if j + k == i:
                        ans.append(arr[k][j])
        
        
        