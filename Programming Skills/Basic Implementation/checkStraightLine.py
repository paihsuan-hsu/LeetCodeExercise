class Solution:
    def checkStraightLine(self, coordinates: list[list[int]])-> bool:
        #  slope = rise/run = (y2-y1)/(x2-x1)
        m = len(coordinates)
        slope = (coordinates[-1][0]-coordinates[0][0])/(coordinates[-1][1]-coordinates[0][1])
        for i in range(m-1):
            if slope != (coordinates[i+1][0]-coordinates[i][0])/(coordinates[i+1][1]-coordinates[i][1]):
                return False
        return True
        
# Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
# Output: true
output = Solution()
coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
print(output.checkStraightLine(coordinates))

# Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
# Output: false
coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
print(output.checkStraightLine(coordinates))