from typing import Optional
class TreeNote:
    def __init__(self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class Tree:
    def inorderTraversal(self, root: Optional[TreeNote])->list[int]:
        notes = []
        def inorder(root: Optional[TreeNote]):
            if root:
                inorder(root.left)
                notes.append(root.val)
                inorder(root.right)
        inorder(root) 
        return notes

    
    def buildTree(self, nums: list[int])->Optional[TreeNote]:
        n1 = TreeNote()
        n2 = TreeNote()
        n3 = TreeNote()
        n1.val=1
        n2.val=2
        n3.val=3
        n1.right=n2
        n2.left=n3
        return n1

# Input: root = [1,null,2,3]
# Output: [1,3,2]
output = Tree()
root = [1,None,2,3]
p=output.inorderTraversal(output.buildTree(root))

for i in p:
    print(i)
    

        

