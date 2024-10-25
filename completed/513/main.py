from icecream import ic as print
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def swap_children(self, node: TreeNode):
        if node:
            tmp = node.right
            node.right = self.swap_children(node.left)
            node.left = self.swap_children(tmp)
        return node

    def last_node(self, root):
        nodes = deque([root])
        last_val = None
        while nodes:
            n = nodes.popleft()
            if n:
                last_val = n.val
                nodes.append(n.left)
                nodes.append(n.right)
        return last_val

    def findBottomLeftValue(self, root) -> int:
        n = self.swap_children(root)
        return self.last_node(n)

if __name__ == '__main__':
    sol = Solution()
    input1 = TreeNode(val=2, left=TreeNode(val=1, left=None, right=None), right=TreeNode(val=3, left=None, right=None))
    print(sol.findBottomLeftValue(input1))
