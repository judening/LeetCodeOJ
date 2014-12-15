class Solution:

    def isBalanced(self,root):
        self.result = True
        self.isBalancedHelper(root)
        return self.result

    #This is a bottom up method. The height is passed up to the upper
    #level. Meanwhile, we want to know if at the bottom level, they're
    #balanced at the first place.
    def isBalancedHelper(self,root):
        if not root:
            return 0
        else:
            left = self.isBalancedHelper(root.left)
            right = self.isBalancedHelper(root.right)
            if(abs(left-right)>1):
                self.result = False
            return max(left,right)+1
