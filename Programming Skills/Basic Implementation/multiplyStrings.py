class Solution:
    def multiply(self, num1:str, num2:str)->str:
        nums = {
            "0":0,
            "1":1,
            "2":2,
            "3":3,
            "4":4,
            "5":5,
            "6":6,
            "7":7,
            "8":8,
            "9":9
        }
        n1=0
        n2=0
        d=1
        for i in reversed(num1) :
            n1 += (nums[i] * d)
            d = d*10
        d=1
        for i in reversed(num2):
            n2 += (nums[i] * d)
            d = d*10

        return str(n1*n2)
    
# Input: num1 = "2", num2 = "3"
# Output: "6"
output=Solution()
num1 = "2"
num2 = "3"
print(output.multiply(num1,num2))

# Input: num1 = "123", num2 = "456"
# Output: "56088"
num1 = "123"
num2 = "456"
print(output.multiply(num1,num2))
