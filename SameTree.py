class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
#Again, it is done thru recurssion
#Easy,brisy.
class Solution:
    def isSameTree(self,p,q):
        if p is None and q is None:
            return True
        else:
            if (p is None and q is not None) or (p is not None and q is None):
                return False
            else:
                if p.val == q.val:
                    return self.isSameTree(p,left,q.left) and self.isSameTree(p.right,q.right)
                else:
                    return False


