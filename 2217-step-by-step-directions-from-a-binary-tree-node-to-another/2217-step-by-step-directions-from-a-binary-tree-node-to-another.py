# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], start: int, dest: int) -> str:
        lca = self.find_lca(root, start, dest)
        start_path = []
        dest_path = []
        self.find_path(lca, start, start_path)
        self.find_path(lca, dest, dest_path)

        direction = []

        direction.extend("U" * len(start_path))
        direction.extend(dest_path)

        return "".join(direction)

    def find_lca(self, node:TreeNode, val1, val2):
        if node is None:
            return None
        if node.val == val1 or node.val == val2:
            return node
        
        left_lca = self.find_lca(node.left, val1, val2)
        right_lca = self.find_lca(node.right, val1, val2)

        if left_lca is None:
            return right_lca
        elif right_lca is None:
            return left_lca
        else:
            return node
        
    def find_path(self, node, target, path):
        if node is None:
            return False

        if node.val == target:
            return True

        path.append("L")
        if self.find_path(node.left, target, path):
            return True
        path.pop()

        path.append("R")
        if self.find_path(node.right, target, path):
            return True
        path.pop()

        return False
        