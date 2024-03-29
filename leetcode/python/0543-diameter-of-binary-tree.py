# path: leetcode\python\0543-diameter-of-binary-tree.py
# link: https://leetcode.com/problems/diameter-of-binary-tree/
# date: 2023-04-10
# leetcode: Easy

from ast import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Recursive DFS approach
        # T: O(n) S: O(n)
        res = [0]

        def dfs(root):
            if not root:
                return -1 # returns -1 because we are adding 1 to the height of the tree, this is an empty tree
            left = dfs(root.left)
            right = dfs(root.right)
            res[0] = max(res[0], 2 + left + right) # returns the equation for finding the diameter of the tree

            return 1 + max(left, right) # returns the equation for finding the height of the tree
        
        dfs(root)
        return res[0]
    