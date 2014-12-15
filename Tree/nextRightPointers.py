class Solution:
    def connect(self,root):
        if not root:
            return
        current = root
        while current:
            nextLevel = current.left
            while current:
                #Connect left to right
                if current.left:
                    current.left.next = current.right
                #Connect right to left (has the same grandparent)
                if current.right and current.next:
                    current.right.next = current.next.left
                #Keep moving to handle siblings' case
                current = current.next
            #Keep moving to handle children's case
            current = nextLevel
