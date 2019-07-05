'''
AVL tree is a self-balancing Binary Search Tree (BST) where the difference between 
heights of left and right subtrees cannot be more than one for all nodes.
Most of the BST operations (e.g., search, max, min, insert, delete.. etc) take O(h) time 
where h is the height of the BST. The cost of these operations may become O(n) for a skewed 
Binary tree. If we make sure that height of the tree remains O(Logn) after every insertion 
and deletion, then we can guarantee an upper bound of O(Logn) for all these operations. 
The height of an AVL tree is always O(Logn) where n is the number of nodes in the tree
'''

class AVL_TREE_NODE:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVL_TREE:
    def __init__(self):
        self.root = None

    def get_height(self, curr):
        if curr is None:
            return 0
        return curr.height

    def get_balance(self, curr):
        if curr is None:
            return 0
        return (self.get_height(curr.left) - self.get_height(curr.right))
        
    def left_rotate(self, curr):
        y = curr.right
        T2 = y.left

        y.left = curr
        curr.right = T2

        curr.height = 1 + max(self.get_height(curr.left),
                              self.get_height(curr.right))
        y.height = 1 + max(self.get_height(y.left),
                           self.get_height(y.right))
        return y
        
    def right_rotate(self, curr):
        y = curr.left
        T3 = y.right

        y.right = curr
        curr.left = T3

        curr.height = 1 + max(self.get_height(curr.left),
                              self.get_height(curr.right))
        y.height = 1 + max(self.get_height(y.left),
                           self.get_height(y.right))
        return y
    
    def avl_insert_util(self, curr, node):
        if curr is None:
            return node
        elif curr.value < node.value:
            curr.right = self.avl_insert_util(curr.right, node)
        else:
            curr.left = self.avl_insert_util(curr.left, node)

        curr.height = 1 + max(self.get_height(curr.left),
                              self.get_height(curr.right))

        balance = self.get_balance(curr)

        if balance > 1:
            if node.value > curr.left.value:
                curr.left = self.left_rotate(curr.left)
            return self.right_rotate(curr)
        elif balance < -1:
            if node.value < curr.right.value:
                curr.right = self.right_rotate(curr.right)
            return self.left_rotate(curr)
        else:
            pass
        return curr
    
    def insert(self, value):
        node = AVL_TREE_NODE(value)
        if (self.root):
            self.root = self.avl_insert_util(self.root, node)
        else:
            self.root = node

    def find_min_node_in_subtree(self, curr):
        while (curr.left is not None):
            curr = curr.left
        return curr

    def avl_delete_util(self, curr, value):
        if curr is None:
            return None
        elif value < curr.value:
            curr.left = self.avl_delete_util(curr.left, value)
        elif value > curr.value:
            curr.right = self.avl_delete_util(curr.right, value)
        else:
            # we found the node to be deleted
            if curr.left is None:
                temp = curr.right
                curr = None
                return temp
            if curr.right is None:
                temp = curr.left
                curr = None
                return temp
            temp = self.find_min_node_in_subtree(curr.right)
            curr.value = temp.value
            curr.right = self.avl_delete_util(curr.right, temp.value)

        if curr is None:
            return None

        curr.height = 1 + max(self.get_height(curr.left),
                              self.get_height(curr.right))

        balance = self.get_balance(curr)
        if balance > 1:
            if (self.get_balance(curr.left) < 0):
                curr.left = self.left_rotate(curr.left)
            return self.right_rotate(curr)
        if balance < -1:
            if (self.get_balance(curr.right) > 0):
                curr.right = self.right_rotate(curr.right)
            return self.left_rotate(curr)
        return curr
                        
    def delete(self, value):
        if (self.root is None):
            print("Tree is empty")
            return
        self.root = self.avl_delete_util(self.root, value)
        
    def preorder_util(self, curr):
        if curr is None:
            return
        print(curr.value),
        self.preorder_util(curr.left)
        self.preorder_util(curr.right)
        
    def preorder(self):
        if self.root is None:
            print("Tree is empty")
            return
        print("Preorder: "),
        self.preorder_util(self.root)
        print("")

if __name__ == "__main__":
    t = AVL_TREE()
    t.preorder()
    t.insert(7)
    t.preorder()
    t.insert(6)
    t.preorder()
    t.insert(5)
    t.preorder()
    t.insert(4)
    t.preorder()
    t.insert(5.5)
    t.preorder()
    t.insert(3)
    t.preorder()
    t.delete(5)
    t.preorder()
    t.delete(6)
    t.preorder()
    t.delete(7)
    t.preorder()


