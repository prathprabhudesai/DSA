''' this is an implementaion of binary search tree '''

class BST_NODE:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BINARY_SEARCH_TREE:
    def __init__(self):
        self.root = None

    @staticmethod
    def insertn(curr, node):
        if (curr.value < node.value):
            if (curr.right != None):
                BINARY_SEARCH_TREE.insertn(curr.right, node)
            else:
                curr.right = node
        else:
            if (curr.left != None):
                BINARY_SEARCH_TREE.insertn(curr.left, node)
            else:
                curr.left = node
        return

    def insert(self, value):
        node = BST_NODE(value)
        if (self.root == None):
            self.root = node
        else:
            BINARY_SEARCH_TREE.insertn(self.root, node)

    @staticmethod
    def preordert(curr):
        if (curr != None):
            print(curr.value),
            BINARY_SEARCH_TREE.preordert(curr.left)
            BINARY_SEARCH_TREE.preordert(curr.right)
        else:
            return
        
    def preorder(self):
        if (self.root == None):
            print("Tree is empty")
        else:
            print("\nPre-order: "),
            BINARY_SEARCH_TREE.preordert(self.root)

    @staticmethod
    def inordert(curr):
        if (curr != None):
            BINARY_SEARCH_TREE.inordert(curr.left)
            print(curr.value),
            BINARY_SEARCH_TREE.inordert(curr.right)
        else:
            return
        
    def inorder(self):
        if (self.root == None):
            print("Tree is empty")
        else:
            print("\nIn-order: "),
            BINARY_SEARCH_TREE.inordert(self.root)

    @staticmethod
    def postordert(curr):
        if (curr != None):
            BINARY_SEARCH_TREE.postordert(curr.left)
            BINARY_SEARCH_TREE.postordert(curr.right)
            print(curr.value),
        else:
            return
        
    def postorder(self):
        if (self.root == None):
            print("Tree is empty")
        else:
            print("\nPost-order: "),
            BINARY_SEARCH_TREE.postordert(self.root)

            
    @staticmethod
    def searcht(curr, value):
        if ((curr is None) or (curr.value == value)):
            return curr

        if (curr.value < value):
            return BINARY_SEARCH_TREE.searcht(curr.right, value)

        return BINARY_SEARCH_TREE.searcht(curr.left, value)
        
    def search(self, value):
        if (self.root == None):
            print("Tree is empty")
        else:
            if (BINARY_SEARCH_TREE.searcht(self.root, value) != None):
                print ("Node with value ", value, " is present in the tree")
            else:
                print ("Node with value ", value, " is not present")

    @staticmethod
    def find_min_node_in_subtree(curr):
        while (curr.left is not None):
            curr = curr.left
        return curr
    
    @staticmethod
    def deleten(curr, value):
        if curr is None:
            return curr
        if value < curr.value:
            curr.left = BINARY_SEARCH_TREE.deleten(curr.left, value)
        elif value > curr.value:
            curr.right = BINARY_SEARCH_TREE.deleten(curr.right, value)
        else:
            if curr.left is None:
                temp = curr.right
                curr = None
                return temp
            elif curr.right is None:
                temp = curr.left
                curr = None
                return temp
            temp = BINARY_SEARCH_TREE.find_min_node_in_subtree(curr.right)
            curr.value = temp.value
            curr.right = BINARY_SEARCH_TREE.deleten(curr.right, temp.value)
        return curr
        
    def delete(self, value):
        if (self.root == None):
            print("Tree is empty")
        BINARY_SEARCH_TREE.deleten(self.root, value)

    @staticmethod
    def convert_to_maximum_sum_util(curr, value):
        if curr is None:
            return
        BINARY_SEARCH_TREE.convert_to_maximum_sum_util(curr.right, value)
        value[0] += curr.value
        curr.value = value[0] - curr.value        
        BINARY_SEARCH_TREE.convert_to_maximum_sum_util(curr.left, value)
        
    def convert_to_maximum_sum(self):
        if self.root is None:
            print("Tree is empty")
            return
        value = [0]
        BINARY_SEARCH_TREE.convert_to_maximum_sum_util(self.root, value)
        
if __name__ == "__main__":
    t = BINARY_SEARCH_TREE()
    t.insert(10)
    t.insert(20)
    t.insert(5)
    t.insert(6)
    t.insert(11)
    #t.inorder()
    t.delete(6)
    #t.inorder()
    t.insert(6)
    t.insert(7)
    t.delete(10)
    t.inorder()
    t.preorder()
    t.convert_to_maximum_sum()
    t.inorder()
    
