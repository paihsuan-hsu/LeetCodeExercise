class Solution:
    @classmethod
    def longestIncreasingPath(self, matrix: list[list[int]])->int:
        m = len(matrix)
        n = len(matrix[0])
        maxPath=0
        dp = [[-1] * (n+1) for x in range(m+1)]

        def walk_over_matrix(i: int, j: int, prev: int)->int:
            if i < 0 or i >= m or j < 0 or j >= n or prev >= matrix[i][j]:
                return 0
            # only check the new cell 
            if dp[i][j] == -1:
                # found max for 4 dir
                dp[i][j]= max(
                    walk_over_matrix(i+1, j,  matrix[i][j]),
                    walk_over_matrix(i-1, j,  matrix[i][j]),
                    walk_over_matrix(i, j+1,  matrix[i][j]),
                    walk_over_matrix(i, j-1,  matrix[i][j])
                ) + 1
            return dp[i][j]

        for i in range(m):
            for j in range(n):
                ans = walk_over_matrix(i, j, -1)
                maxPath = max(maxPath, ans)
        return maxPath

# Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
# Output: 4
# The longest increasing path is [1, 2, 6, 9]
input=[[3,4,5],[3,2,6],[2,2,1]]
output = Solution.longestIncreasingPath(input)
print(output)

# Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
# Output: 4
# The longest increasing path is [3, 4, 5, 6]
input2=[[9,9,4],[6,6,8],[2,1,1]]
output2 = Solution.longestIncreasingPath(input2)
print(output2)