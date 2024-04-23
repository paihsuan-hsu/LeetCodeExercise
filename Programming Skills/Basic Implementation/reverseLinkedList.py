from typing import Optional
class ListNote:
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next

class Solution:
    def add(self, nums:list[int])->Optional[ListNote]:
        output = ListNote()
        dummy = output
        for i in nums:
            nextNote = ListNote()
            nextNote.val = i
            nextNote.next = None
            dummy.next = nextNote
            dummy = dummy.next
        return output.next
    
    def reverseList(self, head: Optional[ListNote])-> Optional[ListNote]:
        current = head
        preNote = None
        nextNote = None

        while current:
            nextNote = current.next
            current.next = preNote
            preNote = current
            current = nextNote

        return preNote
    
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
output = Solution()
head = [1,2,3,4,5]
input = output.add(head)
justPrint = output.reverseList(input)

while justPrint:
    print(justPrint.val)
    justPrint=justPrint.next

# Input: head = [1,2]
# Output: [2,1]
head = [1,2]
input = output.add(head)
justPrint = output.reverseList(input)

while justPrint:
    print(justPrint.val)
    justPrint=justPrint.next

# Input: head = []
# Output: []
head = []
input = output.add(head)
justPrint = output.reverseList(input)

while justPrint:
    print(justPrint.val)
    justPrint=justPrint.next