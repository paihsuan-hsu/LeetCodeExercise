class Solution:
    def addBinary(self, a:str, b: str)->str:
        # can not use bin() or format(11,'b) - 1011
        m = max(len(a), len(b))
        a = a[::-1]
        b = b[::-1]
        carry = 0
        i = 0
        output=""

        while i < m:
            sum = 0
            if i < len(a) and i < len(b):
                sum = int(a[i]) + int(b[i])
            elif i < len(a):
                sum = int(a[i])
            elif i < i < len(b):
                sum = int(b[i])
            sum += carry
            carry = sum//2
            output += str(sum%2)
            i+=1
        
        if carry != 0:
            output += str(carry)

        return output[::-1]
    
# Input: a = "11", b = "1"
# 
output = Solution()
a = "11"
b = "1"
print(output.addBinary(a,b))

# Input: a = "1010", b = "1011"
# Output: "10101"
a = "1010" 
b = "1011"
print(output.addBinary(a,b))
