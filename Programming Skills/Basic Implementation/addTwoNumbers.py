from typing import Optional
class ListNote:
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next
class Solution:
    def add(self, nums:list[int])-> Optional[ListNote]:
        output=ListNote()
        dummy = output
        for i in nums:
            nextNote = ListNote()
            nextNote.val=i
            nextNote.next=None
            dummy.next = nextNote
            dummy = dummy.next
        return output.next
    
    def reverseList(self, input: Optional[ListNote])->Optional[ListNote]:
        current = input
        preNote = None
        nextNote = None

        while current:
            nextNote = current.next
            current.next = preNote
            preNote = current
            current = nextNote
        
        return preNote
    
    def addTwoNumbers(self, num1: Optional[ListNote], num2: Optional[ListNote])->Optional[ListNote]:
        output = ListNote()
        dummy = output
        n1 = self.reverseList(num1)
        n2 = self.reverseList(num2)

        carry = 0
        while n1 or n2:
            sum = 0
            if n1:
                print("n1 is: ", n1.val)
                sum += n1.val
                n1=n1.next
            if n2:
                print("n2 is: ", n2.val)
                sum+= n2.val
                n2=n2.next
            sum = carry + sum

            print("sum is: ", sum)
            carry = sum // 10
            nextNote = ListNote()
            nextNote.val = sum %10
            nextNote.next=None
            dummy.next=nextNote
            dummy=dummy.next
        return output.next

# Input: l1 = [7,2,4,3], l2 = [5,6,4]
# Output: [7,8,0,7]
# 7243+564=7807
output = Solution()
l1 = [7,2,4,3]
l2 = [5,6,4]
input1 = output.add(l1)
input2 = output.add(l2)
outputList = output.addTwoNumbers(input1, input2)
while outputList:
    print(outputList.val)
    outputList=outputList.next