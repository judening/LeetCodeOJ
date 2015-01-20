class Solution:
    # For myself, I figured out the recurrsive method
    # But the postorder[:rootPo] and postorder[rootPo+1:]
    # are the trickiest point of this question.
    # The split point of inorder determine how many nodes there are
    # in the postorder array
    def buildTree(self,inorder,postorder):
        if not inorder:
            return None
        root = TreeNode(postorder[-1])
        rootPo = inorder.index(postorder[-1])
        num = len(postorder)
        # This is really subtle
        root.left = self.buildTree(inorder[:rootPo],postorder[:rootPo])
        root.right = self.buildTree(inorder[rootPo+1:],postorder[rootPo:num-1]
        return root
