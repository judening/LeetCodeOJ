class Solution:
    # Write the inorder traveral
    # Note that it's a ascending order
    # If you notice this, it becomve very obvious
    # Find the first node that is greater than it's next node
    # according to the order, and set it as node1
    # Keep changing node2 until you find a node that is greater than node1
    # Than swap
    def recoverTree(self,root):
        self.node1 = None
        self.node2 = None
        self.prev = None
        self.inorderTraversal(root)
        self.node.val, self.node.val = self.node2.val, self.node1.val
        return root

    # Example: [1,3,8,6,7,4,10,13,14]
    # Notice that 8>6 so node1 = 8
    # Notice that 7>4 so node2 = 4
    def inorderTraverse(self,root):
        if not root:
            return
        self.inorderTraverse(root.left)
        if self.prev:
            # It would happen twice
            if root.val <= self.prev.val:
                # The first encounter
                if not self.node1:
                    self.node1 = self.prev
                self.node2 = root
        self.prev = root
        self.inorderTraverse(root.right)

