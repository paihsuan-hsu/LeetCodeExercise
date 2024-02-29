import math

class Solution:
    @classmethod
    def minimumOperationsToReduceIntegerToZero(self, number: int)-> int:
        count=0
        diff = number
        while diff !=0:
           logNum = math.log2(diff)
           x = round(logNum)
           y = pow(2, x)
           diff = abs(diff-y)
           count+=1
        return count
           
intput = 39 
output = Solution.minimumOperationsToReduceIntegerToZero(intput)
print(output)