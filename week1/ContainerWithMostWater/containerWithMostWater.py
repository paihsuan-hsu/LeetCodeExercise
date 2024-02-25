
class Solution:
    @classmethod 
    def maxArea(self, hight:list) -> int:
        left = 0
        right = len(hight)-1
        area = 0
        max_area = 0
        while left < right:
            area = (right-left) * min(hight[left],hight[right])
            max_area = max(max_area,area)

            if left < right:
               left+=1
            else:
               right-=1
        return max_area

hight = [1,8,6,2,5,4,8,3,7]
output = Solution.maxArea(hight)
print(output)