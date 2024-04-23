from typing import Optional
class ListNote:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next=next
class Solution:
    def add(self, nums: list[int])-> Optional[ListNote]:
        output = ListNote()
        dummy = output

        for i in nums:
            nextNote = ListNote()
            nextNote.val = i
            nextNote.next = None
            dummy.next = nextNote
            dummy = dummy.next
        
        return output.next
    
    def addTwoNumbers(self, num1: Optional[ListNote], num2:Optional[ListNote])->Optional[ListNote]:
        output = ListNote()
        dummy = output
        carry = 0
        while num1 or num2:
            sum = 0 
            if num1:
                sum += num1.val
                num1=num1.next
            if num2:
                sum += num2.val
                num2= num2.next
            
            sum += carry
            carry = sum//10
            nextNote = ListNote()
            nextNote.val = sum%10
            nextNote.next=None
            dummy.next = nextNote
            dummy = dummy.next
        return output.next

# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807

output = Solution()
l1 = [2,4,3]
l2 = [5,6,4]
input1 = output.add(l1)
input2 = output.add(l2)
outputList = output.addTwoNumbers(input1, input2)
while outputList:
    print(outputList.val)
    outputList=outputList.next

# Input: l1 = [0], l2 = [0]
# Output: [0]
l1 = [0]
l2 = [0]
input1 = output.add(l1)
input2 = output.add(l2)
outputList = output.addTwoNumbers(input1, input2)
while outputList:
    print(outputList.val)
    outputList=outputList.next

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
input1 = output.add(l1)
input2 = output.add(l2)
outputList = output.addTwoNumbers(input1, input2)
while outputList:
    print(outputList.val)
    outputList=outputList.next