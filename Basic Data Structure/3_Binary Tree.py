
class TreeNode(object):
    def __init__(self,val):
        self.val = val
        self.left,self.right = None,None


class Travelsal(object):
    def __init__(self):
        self.travelse_path = list()

    def preorder(self,root):
        if root:
            self.travelse_path.append(root.val)
            self.preorder(root.left)
            self.preorder(root.right)

    def inorder(self,root):
        if root:
            self.inorder(root.left)
            self.travelse_path.append(root.val)
            self.inorder(root.right)

    def postorder(self,root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            self.travelse_path.append(root.val)
