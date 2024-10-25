class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)
    
    def search(self, value):
        return self._search_recursive(self.root, value)
    
    def _search_recursive(self, node, value):
        if node is None or node.value == value:
            return node
        
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)
    
    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)
    
    def _delete_recursive(self, node, value):
        if node is None:
            return None
        
        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            # Case 1: Leaf node
            if node.left is None and node.right is None:
                return None
            
            # Case 2: Node with one child
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            
            # Case 3: Node with two children
            min_value = self._find_min(node.right)
            node.value = min_value
            node.right = self._delete_recursive(node.right, min_value)
        
        return node
    
    def _find_min(self, node):
        current = node
        while current.left:
            current = current.left
        return current.value
    
    # Traversal methods
    def inorder(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)
    
    def preorder(self):
        result = []
        self._preorder_recursive(self.root, result)
        return result
    
    def _preorder_recursive(self, node, result):
        if node:
            result.append(node.value)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)
    
    def postorder(self):
        result = []
        self._postorder_recursive(self.root, result)
        return result
    
    def _postorder_recursive(self, node, result):
        if node:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.value)
    
    def height(self):
        return self._height_recursive(self.root)
    
    def _height_recursive(self, node):
        if node is None:
            return -1
        left_height = self._height_recursive(node.left)
        right_height = self._height_recursive(node.right)
        return max(left_height, right_height) + 1

# Example usage:
if __name__ == "__main__":
    tree = BinaryTree()
    
    # Insert values
    values = [5, 3, 7, 1, 4, 6, 8]
    for value in values:
        tree.insert(value)
    
    print("Inorder traversal:", tree.inorder())     # Expected: [1, 3, 4, 5, 6, 7, 8]
    print("Preorder traversal:", tree.preorder())   # Expected: [5, 3, 1, 4, 7, 6, 8]
    print("Postorder traversal:", tree.postorder()) # Expected: [1, 4, 3, 6, 8, 7, 5]
    print("Tree height:", tree.height())            # Expected: 2
    
    # Search for values
    print("Search for 6:", tree.search(6) is not None)  # Expected: True
    print("Search for 9:", tree.search(9) is not None)  # Expected: False
    
    # Delete a value
    tree.delete(3)
    print("After deleting 3:", tree.inorder())      # Expected: [1, 4, 5, 6, 7, 8]