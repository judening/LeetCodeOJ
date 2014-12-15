class Solution:
    def isValidBST(self,root):
        return self.helper(root)

    def helper(self,node):
        if not node:
            return True
        if node.left:
            if node.val > node.left.val:
                rightest = None
                rightest = self.findRightest(node.left).val
                if node.val <= rightest:
                    return False
            else:
                return False
        if node.right:
            if node.val < node.right.val:
                leftest = None
                leftest = self.findLeftest(node.right).val
                if node.val >= leftest:
                    return False
            else:
                return False

        return self.helper(node.left) and self.helper(node.right)

    def findRightest(self,node):
        if node.right:
            return self.findRightest(node.right)
        else:
            return node

    def findLeftest(self,node):
        if node.left:
            return self.findLeftest(node.left)
        else:
            return node
