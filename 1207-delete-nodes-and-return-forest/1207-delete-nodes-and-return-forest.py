# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_del = set(to_delete)
        forest = []

        root = self.process_node(root, to_del, forest)

        if root:
            forest.append(root)
        return forest

    def process_node(self, node, to_del, forest):
        if not node:
            return None
        
        node.left = self.process_node(node.left, to_del, forest)
        node.right = self.process_node(node.right, to_del, forest)

        if node.val in to_del:
            if node.left:
                forest.append(node.left)
            if node.right:
                forest.append(node.right)
            return None
            
        return node
        