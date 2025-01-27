class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def __r_contains(self, node, value):
        if node == None:
            return False
        if value == node.value:
            return True
        elif value < node.value:
            return self.__r_contains(node.left, value)
        elif value > node.value:
            return self.__r_contains(node.right, value)
    
    def r_contains(self, value):
        if self.root is None:
            return False
        return self.__r_contains(self.root, value)


    def __r_insert(self, node, new_node):
        if new_node.value < node.value:
            if node.left is None:
                node.left = new_node
            return self.__r_insert(node.left, new_node)
        elif new_node.value > node.value:
            if node.right is None:
                node.right = new_node
            return self.__r_insert(node.right, new_node)
        elif new_node.value == node.value:
            return False
        return True

    def r_insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        return self.__r_insert(self.root, new_node)
    

    def min_value(self, node):
        while node.left is not None:
            node = node.left
        return node.value
        
        
    def __delete(self, node, value):
        if node is None:
            return None
        if value < node.value:
            node.left = self.__delete(node.left, value)
        elif value > node.value:
            node.right = self.__delete(node.right, value)
        else:
            if node.left == None and node.right == None:
                return None
            if node.left == None:
                return node.right
            if node.right == None:
                return node.left
            
            node.value = self.min_value(node.right)
            node.right = self.__delete(node.right, node.value)
            return node
            
    def delete_node(self, value):
        if self.root is None:
            return False
        return self.__delete(self.root, value)

    def __invert_tree(self, node):
        if node.left:
            self.__invert_tree(node.left)
        if node.right:
            self.__invert_tree(node.right)
        node.left, node.right = node.right, node.left

    def invert(self):
        if not self.root:
            return None
        return self.__invert_tree(self.root)

    # The 'is_balanced' and 'inorder_traversal' methods will 
    # be used to test your code
    def is_balanced(self, node=None):
        def check_balance(node):
            if node is None:
                return True, -1
            left_balanced, left_height = check_balance(node.left)
            if not left_balanced:
                return False, 0
            right_balanced, right_height = check_balance(node.right)
            if not right_balanced:
                return False, 0
            balanced = abs(left_height - right_height) <= 1
            height = 1 + max(left_height, right_height)
            return balanced, height

        balanced, _ = check_balance(self.root if node is None else node)
        return balanced
        
    def inorder_traversal(self, node=None):
        if node is None:
            node = self.root
        result = []
        self._inorder_helper(node, result)
        return result
    
    def _inorder_helper(self, node, result):
        if node:
            self._inorder_helper(node.left, result)
            result.append(node.value)
            self._inorder_helper(node.right, result)
                
                
    def sorted_list_to_bst(self, nums):
        self.root = self.__sorted_list_to_bst(nums, 0, len(nums) - 1)

    def __sorted_list_to_bst(self, nums, left, right):
        if left > right:
            return None
        hlf = (left + right) // 2
        new_node = Node(nums[hlf])

        new_node.left = self.__sorted_list_to_bst(nums, left, hlf - 1)
        new_node.right = self.__sorted_list_to_bst(nums, hlf + 1, right)
        
        return new_node            


def check_balanced_and_correct_traversal(bst, expected_traversal):
    is_balanced = bst.is_balanced()
    inorder = bst.inorder_traversal()
    print("Is balanced:", is_balanced)
    print("Inorder traversal:", inorder)
    print("Expected traversal:", expected_traversal)
    if is_balanced and inorder == expected_traversal:
        print("PASS: Tree is balanced and inorder traversal is correct.\n")
    else:
        print("FAIL: Tree is either not balanced or inorder traversal is incorrect.\n")

# Test: Convert an empty list
print("\n----- Test: Convert Empty List -----\n")
bst = BinarySearchTree()
bst.sorted_list_to_bst([])
check_balanced_and_correct_traversal(bst, [])

# Test: Convert a list with one element
print("\n----- Test: Convert Single Element List -----\n")
bst = BinarySearchTree()
bst.sorted_list_to_bst([10])
check_balanced_and_correct_traversal(bst, [10])

# Test: Convert a sorted list with odd number of elements
print("\n----- Test: Convert Sorted List with Odd Number of Elements -----\n")
bst = BinarySearchTree()
bst.sorted_list_to_bst([1, 2, 3, 4, 5])
check_balanced_and_correct_traversal(bst, [1, 2, 3, 4, 5])

# Test: Convert a sorted list with even number of elements
print("\n----- Test: Convert Sorted List with Even Number of Elements -----\n")
bst = BinarySearchTree()
bst.sorted_list_to_bst([1, 2, 3, 4, 5, 6])
check_balanced_and_correct_traversal(bst, [1, 2, 3, 4, 5, 6])

# Test: Convert a large sorted list
print("\n----- Test: Convert Large Sorted List -----\n")
bst = BinarySearchTree()
large_sorted_list = list(range(1, 16))  # A list from 1 to 15
bst.sorted_list_to_bst(large_sorted_list)
check_balanced_and_correct_traversal(bst, large_sorted_list)


