class Solution:
    def solve(self, prestart, poststart, preend, preorder, postorder):
        if prestart > preend:
            return None

        root = TreeNode(preorder[prestart])
        if prestart == preend:
            return root
        
        next_node = preorder[prestart + 1]  # Root of left subtree
        
        j = poststart
        while postorder[j] != next_node:
            j += 1
        
        num = j - poststart + 1
        
        root.left = self.solve(prestart + 1, poststart, prestart + num, preorder, postorder)
        root.right = self.solve(prestart + num + 1, j + 1, preend, preorder, postorder)
        
        return root

    def constructFromPrePost(self, preorder, postorder):
        n = len(preorder)
        return self.solve(0, 0, n - 1, preorder, postorder)
