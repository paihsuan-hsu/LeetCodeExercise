class Solution:
    @classmethod
    def countSqaures(self, matrix: list[list[int]])->int:
        m = len(matrix)
        n = len(matrix[0])
        dpm = m+1
        dpn = n+1
        dp = [[0]*(n+1) for x in range(m+1)]
        sq = 0
        for i in range (m):
            for j in range(n):
                if(matrix[i][j]==1):
                    dp[i+1][j+1] = min(dp[i][j],dp[i+1][j],dp[i][j+1])+1
                    sq += dp[i+1][j+1]
        
        return sq
    
matrix = [[1,0,1], [1,1,0], [1,1,0]] 
output = Solution.countSqaures(matrix)
print(output)
# m * n
# [1,0,1]
# [1,1,0]
# [1,1,0]

# size 1x1 is 6
# size 2x2 is 1
# size 3x3 is 0
# found = 7