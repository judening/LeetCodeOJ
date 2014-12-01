class Solution:
    #This is the most standard solution.
    #Just recurssively run through the Tree.
    #I will do the breath search first one in the other directory
    def preorderTraversal(self,root):
        self.output = []
        self.helper(root)
        return self.output

    def helper(self,root):
        if not root:
            return
        else:
            self.output.append(root.val)
            self.helper(root.left)
            self.helper(root.right)
