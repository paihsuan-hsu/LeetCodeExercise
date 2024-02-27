class Solution:
    @classmethod
    def twoSum(self, numbers: list[int], taregt: int)->list[int]:
        output = []
        n = len(numbers)
        for i in range (n):
            for j in range (i+1, n):
                if numbers[i]+numbers[j]==target:
                    output.append(i)
                    output.append(j)
                    return output

        return output

input = [2,7,11,15]
target = 9
printOut = Solution.twoSum(input, target)
print(printOut)