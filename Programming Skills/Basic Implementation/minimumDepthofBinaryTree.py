from typing import Optional
class TreeNote:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class Tree:
    def minDepth(self, root: Optional[TreeNote])->int:
        if root is None:
            return 0
        
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        
        return min(left, right) +1
    
    def buildTree(self, nums: list[int])-> Optional[TreeNote]:
        n1 = TreeNote()
        n2 = TreeNote()
        n3 = TreeNote()
        n4 = TreeNote()
        n5 = TreeNote()
        n1.val=3
        n2.val=9
        n3.val=20
        n4.val=15
        n5.val=7
        n1.left=n2
        n1.right=n3
        n3.left=n4
        n3.right=n5

        return n1

# Input: root = [3,9,20,null,null,15,7]
# Output: 2
root = [3,9,20,None,None,15,7]    
output=Tree()
print(output.minDepth(output.buildTree(root)))

# Input: root = [2,null,3,null,4,null,5,null,6]
# Output: 5