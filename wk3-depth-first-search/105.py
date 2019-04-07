# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree_v1(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None

        root = TreeNode(preorder.pop(0))
        root_idx = inorder.index(root.val)

        left_inorder = inorder[:root_idx]
        right_inorder = inorder[root_idx + 1:]

        if left_inorder:
            root.left = self.buildTree(preorder, left_inorder)
        if right_inorder:
            root.right = self.buildTree(preorder, right_inorder)

        return root

    def buildTree_v2(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None

        d = {}
        for idx, val in enumerate(inorder):
            d[val] = idx

        def helper(start, end):
            val = preorder.pop(0)
            node = TreeNode(val)
            idx = d[val]

            if idx > start:
                node.left = helper(start, idx)
            if idx + 1 < end:
                node.right = helper(idx + 1, end)

            return node

        return helper(0, len(inorder))

    def buildTree_v3(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None

        root = TreeNode(preorder[0])
        stack = [root]
        inorder_index = 0

        for i in range(1, len(preorder)):
            node = TreeNode(preorder[i])
            prev = None

            while stack and stack[-1].val == inorder[inorder_index]:
                prev = stack.pop()
                inorder_index += 1
            if prev:
                prev.right = node
            else:
                stack[-1].left = node

            stack.append(node)

        return root
