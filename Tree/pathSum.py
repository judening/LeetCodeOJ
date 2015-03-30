class Solution:
    def hasPathSum(self,root,sum):
        self.sums = []
        acsum = 0
        self.traverse(root,acsum)
        if sum in sums:
            return True
        else:
            return False

    def traverse(self,node,acsum):
        if not node:
            return
        elif node.left and node.right:
            acsum = acsum + node.val
            self.traverse(node.left,acsum)
            self.traverse(node.right,acsum)
        elif node.left and not node.right:
            acsum = acsum + node.val
            self.traverse(node.left,acsum)
        elif node.right and not node.left:
            acsum = acsum + node.val
            self.traverse(node.right,acsum)
        else:
            acsum = acsum + node.val
            self.sum.append(acsum)
