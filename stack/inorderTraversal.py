class Solution:

    def inorderTraversal(self,root):
        stack = []
        output = []
        if not root:
            return output
        while True:
            if root:
                #This makes sure we get the deepest level of left subtree
                #before we pop anything
                stack.append(root)
                root = root.left
            else:
                if not stack:
                    break
                else:
                    root = stack.pop()
                    output.append(root.val)
                    #Then we think about the right subtree
                    root = root.right
        return output
