class Solution:
    # Use a List as queue, then do the BFS iteratively
    def levelOrder(self,root):
        if not root:
            return []
        ans = []
        cur = []
        q = [root,None]
        while len(q) >0:
            node = q.pop(0)
            if node == None:
                if len(cur)>0:
                    ans.insert(0,cur)
                    cur = []
                    q.append(None)
            else:
                cur.append(node.val)
                if node.left != None:
                    q.append(node.val)
                if node.right != None:
                    q.append(node.right)
        return ans
