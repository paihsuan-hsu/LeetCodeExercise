class Solution:
    @classmethod
    def countPathsinGrid(self, grid: list[list[int]])->int:
        m = len(grid)
        n = len(grid[0])
        paths = 0       
        dp = [[-1] * n for x in range(m)]
        
        def walk_over_grid(i: int, j: int, prev: int, checking: int):
            cout = 1
            # make sure it's not out of range
            if i < 0 or i >= m or j < 0 or j >= n or prev >= grid[i][j]:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            # only checking unvisted cell
            directions = [[1,0], [-1,0], [0,1],[0,-1]]
            if dp[i][j] == -1:
                for dir in directions:
                    cout += walk_over_grid(i+dir[0], j+dir[1], grid[i][j], checking+1)
            dp[i][j] = cout
            return cout

        for i in range(m):
            for j in range(n):
                paths += walk_over_grid(i, j, -1, 1)
    
        # return it modulo 10^9 + 7.
        mod = (int)(1e9+7)
        return paths % mod

# Input: grid = [[1,1],[3,4]]
# Output: 8

input = [[1,1],[3,4]]
output = Solution.countPathsinGrid(input)
print(output)

# Input: grid = [[1],[2]]
# Output: 3
input2 = grid = [[1],[2]]
output2 = Solution.countPathsinGrid(input2)
print(output2)