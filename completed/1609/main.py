from icecream import ic as print
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def test_val(self, vals, level):
        cond1 = vals[-1] % 2
        if not level % 2:
            if len(vals) == 2:
                cond2 = vals[0] < vals[1]
            else:
                cond2 = True
            return cond1 and cond2
        else:
            if len(vals) == 2:
                cond2 = vals[0] > vals[1]
            else:
                cond2 = True
            return not cond1 and cond2

    def get_levels(self, root):
        levels = deque([[root]])
        level_cntr = 0
        vals = [[root.val]]
        if not self.test_val([root.val], level_cntr):
            return False
        while levels:
            level_cntr += 1
            level = levels.popleft()
            new_level = []
            new_level_vals = []
            for node in level:
                for nc in [node.left, node.right]:
                    if nc:
                        new_level.append(nc)
                        new_level_vals.append(nc.val)
                        if new_level_vals[-2:] and not self.test_val(new_level_vals[-2:], level_cntr):
                            return False
            if new_level:
                levels.append(new_level)
                vals.append(new_level_vals)
        return True

    def isEvenOddTree(self, root: TreeNode):
        res = self.get_levels(root)
        return res



if __name__ == '__main__':
    sol = Solution()
    input1 = TreeNode(val=1, left=TreeNode(val=10, left=TreeNode(val=3, left=TreeNode(val=12, left=None, right=None), right=TreeNode(val=8, left=None, right=None)), right=None), right=TreeNode(val=4, left=TreeNode(val=7, left=TreeNode(val=6, left=None, right=None), right=None), right=TreeNode(val=9, left=None, right=TreeNode(val=2, left=None, right=None))))
    input2 = TreeNode(val=2, left=TreeNode(val=10, left=TreeNode(val=3, left=TreeNode(val=12, left=None, right=None), right=TreeNode(val=8, left=None, right=None)), right=None), right=TreeNode(val=4, left=TreeNode(val=7, left=TreeNode(val=6, left=None, right=None), right=None), right=TreeNode(val=9, left=None, right=TreeNode(val=2, left=None, right=None))))
    print(sol.isEvenOddTree(input1))
    print(sol.isEvenOddTree(input2))
