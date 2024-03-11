# Given the root of a binary tree, return the inorder traversal of its nodes' values.

# Test1: 
  # Input: root = [1,null,2,3]
  # Output: [1,3,2]

# Test2: 
  # Input: root = []
  # Output: []


class TreeNode:
  def __init__(self, val=0, left=None, right=None):
    self.left = left
    self.right = right
    self.val = val


class DFS:
  def inorderTraversal(self, root = None):
    if not root:
      return []
    stack = []
    res = [] 
    while stack or root:
      if root:
        stack.append(root)
        root = root.left
      else:
        root = stack.pop()
        res.append(root.val)
        root = root.right
    return res


# first input  
node = TreeNode(1)
node.right = TreeNode(2)
node.right.left = TreeNode(3)


dfs = DFS()
inorder_1 = dfs.inorderTraversal(node)

# second input 
inorder_2 = dfs.inorderTraversal()

print(inorder_1)
print(inorder_2)