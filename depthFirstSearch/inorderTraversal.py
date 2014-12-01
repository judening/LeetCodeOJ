class Solution:

    def inorderTraversal(self,root):
        self.output = []
        self.helper(root)
        return self.output

    def helper(self,root):
        if not root:
            return
        else:
            self.helper(root.left)
            self.out.append(root.val)
            self.helper(root.right)
