class Solution:
    def postorderTraversal(self,root):
        queue = []
        self.tehRealTraversal(root,queue)
        return queue

    def tehRealTraversal(self,root,queue):
        if root:
            if root.left:
                self.tehRealTraversal(root.left,queue)
            if root.right:
                self.tehRealTraversal(root.right,queue)
            queue.append(root.val)
