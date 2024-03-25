class Solution:
    @classmethod
    def maximalSquare(self, maxtrix: list[list[int]])->int:
        m = len(maxtrix)
        n = len(maxtrix[0])
        ans = 0
        maxSquare=0
        dp = [[0] * (n+1) for x in range(m+1)]

        for i in range(m):
            for j in range(n):
                if(maxtrix[i][j]==1):
                    dp[i+1][j+1] = min(dp[i][j], dp[i][j+1], dp[i+1][j])+1
                    maxSquare = max(maxSquare, dp[i+1][j+1])
        return maxSquare * maxSquare

input = [[1,0,1,0,0],
         [1,0,1,1,1],
         [1,1,1,1,1],
         [1,0,0,1,0]]
output = Solution.maximalSquare(input)
print(output)