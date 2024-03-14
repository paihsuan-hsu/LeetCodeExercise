from typing import Optional
class ListNode:
    @classmethod
    def __intit__(self, value, next):
        self.value = value
        self.next = next
class Solution:
    @classmethod
    def deleteNode(self, input: Optional[ListNode], target:int)->Optional[ListNode]:
        output = input
        dummy = output
        while dummy:
            if dummy.value == target:
                dummy.value = dummy.next.value
                dummy.next = dummy.next.next

            dummy=dummy.next
        return output
    
#head = [4,5,1,9], node = 5 Output: [4,1,9]
input1 = ListNode()
input1.value=9
input1_1 = ListNode()
input1_1.value=1
input1_2 = ListNode()
input1_2.value=5
input1_3 = ListNode()
input1_3.value=4
input1.next=input1_1
input1_1.next=input1_2
input1_2.next=input1_3
input1_3.next=None
target=5
output = ListNode()
output = Solution.deleteNode(input1, target)

while output:
    print(output.value)
    output=output.next