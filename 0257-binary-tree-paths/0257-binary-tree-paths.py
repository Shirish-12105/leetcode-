class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        result = []
        
        def walk(node, path):
            if not node:  # If the node is empty, stop
                return
                
            # Add current node to path
            if path:
                path += "->" + str(node.val)
            else:
                path = str(node.val)
                
            # If it's a leaf, save it!
            if not node.left and not node.right:
                result.append(path)
                return
                
            walk(node.left, path)
            walk(node.right, path)
            
        walk(root, "")
        return result