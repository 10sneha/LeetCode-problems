# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        return self.post_order(root, distance)[11]

    def post_order(self, node, distance):
        if node is None:
            return [0] * 12
        elif node.left is None and node.right is None:
            curr = [0] * 12
            curr[0] = 1
            return curr
        
        left = self.post_order(node.left, distance)
        right = self.post_order(node.right, distance)

        curr = [0] * 12

        for i in range(10):
            curr[i+1] += left[i] + right[i]

        curr[11] = left[11] + right[11]

        for d1 in range(distance + 1):
            for d2 in range(distance + 1):
                if 2 + d1 +d2 <= distance:
                    curr[11] += left[d1] * right[d2]

        return curr