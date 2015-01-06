class Solution:
    # Pre-order : root-left-right
    # Post-order : left-right-root
    # In-order : left-root-right
    # Pre-order traversal is root-left-right, and post order is left-right-root
    # Modify the code for pre-order to make it root-right-left, and then
    # reverse the output so that we can left-right-root
    def postorderTraversal(self,root):
        stack = []
        output = []
        if root:
            stack.append(root)
        while stack:
            pop = stack.pop()
            output.append(pop.val)
            if pop.left:
                stack.append(pop.left)
            if pop.right:
                stack.append(pop.right)

        output.reverse()
        return output
