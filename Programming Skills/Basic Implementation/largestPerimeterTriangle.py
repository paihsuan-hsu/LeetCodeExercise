class Solution:
    def largestPerimeter(self, nums: list[int])->int:
        side1 = 0
        side2 = 0
        side3 = 0
        n = len(nums)
        if len(nums) < 3:
            return 0
        nums.sort()
        for i in range(n-1, 1, -1):
            print(nums[i],nums[i-1],nums[i-2])
            # sum takes an iterable object such as a list - sum([a, b]) or tuple - sum((a, b)): 
            if nums[i] < sum((nums[i-1], nums[i-2])):
                return nums[i] + nums[i-1] + nums[i-2]
        return 0

# Input: nums = [2,1,2]
# Output: 5
output=Solution()
nums = [2,1,2]
print(output.largestPerimeter(nums))
# Input: nums = [1,2,1,10]
# Output: 0
nums = [1,2,1,10]
print(output.largestPerimeter(nums))
