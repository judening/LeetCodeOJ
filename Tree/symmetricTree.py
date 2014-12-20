class Solution:

    def isSymmertric(self,root):
        if not root:
            return True
        else:
            return self.isMirror(root.left,root.right)

    def isMirror(self,left,right):
        if not left and not right:
            return True
        if not left or not right:
            return False

        #OMG, the inpair outpair idea is fucking genius
        if left.val == right.val:
            outPair = self.isMirror(left.left,right.right)
            inPair = self.isMirror(left.right,right.left)
            return outPair and inPair
        else:
            return False
