class Solution:
    #Probably the best method of all three methods(DFS,BFS,and Queue)
    def connect(self,root):
        if not root:
            return
        if root.left:
            root.left.next = root.right
            if root.next is None:
                root.right.next = None
            else:
                root.right.next = root.next.left

            #Do this to the left
            self.connect(root.left)
            #Do this to the right
            self.connect(root.right)

        return
