class Solution:
    def diagonalSum(self, mat: list[list[int]])-> int:
        left=0
        right=len(mat)-1
        primaryDiagonal=[]
        secondaryDiagonal=[]

        while left<=len(mat)-1 and right>=0:
            primaryDiagonal.append(mat[left][left])
            secondaryDiagonal.append(mat[right][right])
            left +=1
            right -=1
        
        overLap = 0
        if len(primaryDiagonal)//2 % 2 != 0 or len(primaryDiagonal)<=1:
            overLap = primaryDiagonal[len(primaryDiagonal)//2]
        
        return sum(primaryDiagonal, sum(secondaryDiagonal)) - overLap
    

# Input: mat = [[1,2,3],
#               [4,5,6],
#               [7,8,9]]
# Output: 25
output = Solution()
mat = [[1,2,3],[4,5,6],[7,8,9]]
print(output.diagonalSum(mat))

# Input: mat = [[1,1,1,1],
#               [1,1,1,1],
#               [1,1,1,1],
#               [1,1,1,1]]
# Output: 8
mat = [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]
print(output.diagonalSum(mat))


# Input: mat = [[5]]
# Output: 5
mat = [[5]]
print(output.diagonalSum(mat))
