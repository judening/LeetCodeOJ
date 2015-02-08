# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# This problem is very similar to construct a BST based on a sorted array/sorted
# linkedlist
class Solution:
    # @return a list of tree node
    def generateTrees(self, n):
        return self.gen(1,n)

    def gen(self, start, end):
        # return a list containing all root nodes of BSTs constructred from
        # [Start,End]

        if start > end: return [None]
        res = []
        # Take [1,2,3] as example, we start with 1
        # Take it out of the list, we only have [2,3] left on the right
        for rootVal in xrange(start,end+1):
            # For case 1, nothing on the left
            leftList = self.gen(start,rootVal-1)
            # For case 2, whatever left on the list is constructed as BST
            # based on the BST rule
            rightList = self.gen(rootVal+1,end)
            for i in leftList:
                for j in rightList:
                    root = TreeNode(rootVal)
                    root.left = i
                    root.right = j
                    # In this for loop, we just connect the left and right with the
                    # rootval
                    res.append(root)
        return res
