class Solution:
    def levelOrder(self,root):
        if not root:
            return []
        ans = []
        cur = [root]
        while len(cur) >0:
            vals = []
            next = []
            for x in cur:
                vals.append(x.val)
                if x.left is not None:
                    next.append(x.left)
                if x.right is not None:
                    next.append(x.right)
            ans.insert(0,vals)
            cur = next
        return ans
