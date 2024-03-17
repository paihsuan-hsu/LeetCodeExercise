class Solution:
    @classmethod
    def addBinary(self, num1: str, num2: str)->str:
        carry=0
        i= len(num1) - 1
        j= len(num2) - 1
        output=""
        while i >= 0 or j >=0 or carry:
            sum=0
            if i >=0:
                sum+=int(num1[i])
            if j >=0:
                sum+=int(num2[j])
            sum += carry
            carry = sum//2
            output = output + str(sum%2)
            i-=1
            j-=1
        return output[::-1]

#Input: a = "11", b = "1" Output: "100"
a="11"
b="1"
output=Solution.addBinary(a,b)
print(output)
