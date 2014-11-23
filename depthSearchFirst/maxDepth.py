class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self,root):
        #So I think the most straightforward way is just to run a recurssion
        #return the max num of the two
        num = self.findMax(root,0)
        return num

    def findMax(self,node,num):
        #This recurssion that actually return the max num
        if node is None:
            return num
        else:
            num = num + 1
            return max(self.findMax(node.left,num),self.findMax(node.right,num))


solution = Solution()
testTree = TreeNode(1)
testTree0 = TreeNode(2)
testTree1 = TreeNode(3)
testTree2 = TreeNode(4)
testTree3 = TreeNode(5)
testTree.left = testTree0
testTree.right = testTree1
testTree0.left = testTree2
testTree2.left = testTree3

print solution.maxDepth(testTree)
