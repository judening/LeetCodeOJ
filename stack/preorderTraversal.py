class Solution:

    def preorderTraversal(self,root):
        stack = []
        output = []

        if root:
            stack.append(root)
        while stack:
            pop = stack.pop()
            output.append(pop.val)
            if pop.right:
                stack.append(pop.right)
            if pop.left:
                stack.append(pop.left)

        return output
