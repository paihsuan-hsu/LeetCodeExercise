from typing import Optional
class ListNode:
    @classmethod
    def __intit__ (self, value, next):
        self.value=value
        self.next=next
class Solution:
    @classmethod
    def doubleTheNumber(self, head:Optional[ListNode])->Optional[ListNode]:
        output = ListNode()
        dummy = output
        carry =0//10
        while head or carry:
            db=0
            if head:
                x=head.value
                head=head.next
                db = x*2

            db+=carry
            carry = db//10
            tmp = ListNode()
            tmp.value=db%10
            tmp.next=None
            dummy.next=tmp
            dummy=dummy.next

        return output.next


#input [1,8,9] and output should be [3,7,8]
input1 = ListNode()
input1_1 = ListNode()
input1_2 = ListNode()
input1.value=9
input1.next=input1_1
input1_1.value=8
input1_1.next=input1_2
input1_2.value=1
input1_2.next=None
output = ListNode()
output = Solution.doubleTheNumber(input1)
while output:
    print(output.value)
    output=output.next

#input [9,9,9] and output should be [1,9,9,8]
input2 = ListNode()
input2_1 = ListNode()
input2_2 = ListNode()
input2.value=9
input2.next=input2_1
input2_1.value=9
input2_1.next=input2_2
input2_2.value=9
input2_2.next=None
output2 = ListNode()
output2 = Solution.doubleTheNumber(input2)
while output2:
    print(output2.value)
    output2=output2.next