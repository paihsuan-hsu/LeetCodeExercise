
#Note that you must do this in-place without making a copy of the array.

class Solution:
    @classmethod
    def moveZeroes(self, num: list[int])->None:
        n = len(num)
        left = 0
        for right in range(n):
            if num[right] != 0 and num[left]==0:
                num[right], num[left] = num[left], num[right]
            if num[left]!=0:
                left+=1
               
        print(num)
    
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
nums = [0,1,0,3,12]
print(nums)
Solution.moveZeroes(nums)

# Input: nums = [0]
# Output: [0]
nums = [0]
print(nums)
Solution.moveZeroes(nums)


