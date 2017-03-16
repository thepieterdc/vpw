class BinarySearchTree:
    def __init__(self, data=None):
        self.left = None
        self.right = None
        self.data = data

    def __repr__(self):
        return str(self.data)

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is not None:
                    self.left.insert(data)
                else:
                    self.left = BinarySearchTree(data)
            elif data > self.data:
                if self.right is not None:
                    self.right.insert(data)
                else:
                    self.right = BinarySearchTree(data)
        else:
            self.data = data

    def lookup(self, data, parent=None):
        """
        Returns the node and its parent
        """
        if data < self.data:
            if self.left is None:
                return None, None
            return self.left.lookup(data, self)
        elif data > self.data:
            if self.right is None:
                return None, None
            return self.right.lookup(data, self)
        else:
            return self, parent

    def children(self) -> int:
        count = 0
        if self.left:
            count += 1
        if self.right:
            count += 1
        return count

    def delete(self, data):
        node, parent = self.lookup(data)
        if node:
            childs = node.children
            if childs == 0:
                if parent.left is node:
                    parent.left = None
                else:
                    parent.right = None
                del node
            elif childs == 1:
                if node.left:
                    child = node.left
                else:
                    child = node.right
                if parent:
                    if parent.left is node:
                        parent.left = child
                    else:
                        parent.right = child
                del node
            else:
                parent = node
                successor = node.right
                while successor.left:
                    parent = successor
                    successor = successor.left
                node.data = successor.data
                if parent.left == successor:
                    parent.left = successor.right
                else:
                    parent.right = successor.right
