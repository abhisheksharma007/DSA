class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else: 
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        if self.root is None:
            return False
        temp = self.root
        while (temp):
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

  
    def BFS(self):
        if not self.root:
            return []
        queue = [self.root]
        result = [self.root.value]
        while queue:
            if queue[0].left:
                queue.append(queue[0].left)
                result.append(queue[0].left.value)
            if queue[0].right:
                result.append(queue[0].right.value)
                queue.append(queue[0].right)
            queue.pop(0)
        return result
    
    def traverse_pre_order(self, node, results):
        results.append(node.value)
        if node.left:
            self.traverse_pre_order(node.left, results)
        if node.right:
            self.traverse_pre_order(node.right, results)
        return results
    
    def dfs_pre_order(self):
        results = []
        if not self.root:
            return results
        return self.traverse_pre_order(self.root, results)
    
    def traverse_post_order(self, node, results):
        if node.left:
            self.traverse_post_order(node.left, results)
        if node.right:
            self.traverse_post_order(node.right, results)
        results.append(node.value)
        return results

    def dfs_post_order(self):
        results = []
        if not self.root:
            return results
        return self.traverse_post_order(self.root, results)

    def traverse_in_order(self, node, results):
        if node.left:
            self.traverse_in_order(node.left, results)
        results.append(node.value)
        if node.right:
            self.traverse_in_order(node.right, results)
        return results
    
    def dfs_in_order(self):
        results = []
        if not self.root:
            return results
        return self.traverse_in_order(self.root, results)
    
    def is_valid_bst(self):
        in_order_res = self.dfs_in_order()
        for i in range(len(in_order_res)):
            if i == 0:
                continue
            if in_order_res[i] < in_order_res[i-1]:
                return False
        return True
    
    
    
    def kth_smallest(self, k):
        if not self.root or k < 1:
            return None
        v = []
        res = []
        def __kth_smallest(node, k, v):
            if node.left:
                __kth_smallest(node.left, k, v)
            v.append(node.value)
            if len(v) == k:
                return res.append(v[k-1])
            if node.right:
                __kth_smallest(node.right, k, v)
        __kth_smallest(self.root, k, v)
        if not res: res.append(None)
        return res[0]

bst = BinarySearchTree()

bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(2)
bst.insert(4)
bst.insert(6)
bst.insert(8)

print(bst.kth_smallest(1))  # Expected output: 2
print(bst.kth_smallest(3))  # Expected output: 4
print(bst.kth_smallest(6))  # Expected output: 7


"""
    EXPECTED OUTPUT:
    ----------------
    2
    4
    7

 """