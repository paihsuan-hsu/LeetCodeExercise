class Solution:
    def setMatrixZeroes(self, matrix: list[list[int]])-> list[list[int]]:
        m = len(matrix)
        n = len(matrix[0])
        ouputMatrix = matrix
        positionSet =[]

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    positionSet.append([i,j])


        x=0
        print("len(positionSet) is: ",len(positionSet))
        while x < len(positionSet):
            walkerA=0
            walkerB=0
            while walkerA < m:
                ouputMatrix[walkerA][positionSet[x][1]]=0
                walkerA+=1
            while walkerB < n:
                ouputMatrix[positionSet[x][0]][walkerB]=0
                walkerB+=1
            x+=1

        return ouputMatrix

# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]
output = Solution()
matrix = [[1,1,1],[1,0,1],[1,1,1]]
print(output.setMatrixZeroes(matrix))

# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
print(output.setMatrixZeroes(matrix))
