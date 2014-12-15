class Solution:
    #This is pretty brillian
    def sortedArrayToBST(self,num):
        return self.createBST(num,0,len(num)-1)

    #Thought process: think about this, you are converting a sorted array
    #to BST. Ultimately, the structure of bst requires you to search the array
    #in the binary way.
    #This is binary search
    def createBST(self,num,start,end):
        if start > end: return None
        mid = (start + end)/2
        root = TreeNode(num[mid])
        root.left = self.createBST(num,start,mid-1)
        root.right = self.createBST(num,mid+1,end)
        return root
