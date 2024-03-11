from typing import Optional
class ListNode:
    @classmethod
    def __intit__(self, value, next):
        self.value = value
        self.next = next
class Solution:
    @classmethod
    def addTowNumbers(self, num1: Optional[ListNode], num2: Optional[ListNode])->Optional[ListNode]:
        output = ListNode()
        dummy = output
        carry=0
        while num1 or num2 or carry:
            sum=0
            if num1:
                x =num1.value
                sum += x
                num1=num1.next
            if num2:
                y=num2.value
                sum += y
                num2=num2.next
            print(x, y, sum, carry)
            sum += carry
            carry = sum//10
            nextNode = ListNode()
            nextNode.value= sum%10
            nextNode.next=None
            dummy.next=nextNode
            dummy = dummy.next
        return output.next

#l1 = [2,4,3], l2 = [5,6,4]
#// output = [8,0,7]
input1 = ListNode()
input1.value=3
input1_1 = ListNode()
input1_1.value=4
input1_2 = ListNode()
input1_2.value=2
input2 = ListNode()
input2.value=4
input2_1 = ListNode()
input2_1.value=6
input2_2 = ListNode()
input2_2.value=5
input1.next=input1_1
input1_1.next=input1_2
input1_2.next = None
input2.next=input2_1
input2_1.next=input2_2
input2_2.next = None

output = ListNode()
output = Solution.addTowNumbers(input1, input2)

while output: # input1.next will fail in endof the list
    print(output.value)
    output=output.next



