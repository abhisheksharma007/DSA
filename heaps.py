class MaxHeap:
    def __init__(self):
        self.heap = []
        
    def _left_child(self, index):
        return 2 * index + 1
    
    def _right_child(self, index):
        return 2 * index + 2
    
    def _parent(self, index):
        return (index-1) // 2
    
    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]
        
    def _heapify_up(self):
        curr_index = len(self.heap) - 1
        parent_index = self._parent(curr_index)
        while self.heap[curr_index] > self.heap[parent_index] and curr_index > 0:
               self._swap(curr_index, self._parent(curr_index))
               curr_index = self._parent(curr_index)
               parent_index = self._parent(curr_index)
        return True
   
    def insert(self, value):
        self.heap.append(value)
        if len(self.heap) > 1:
            self._heapify_up()
        return True
        
    def remove(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        self._swap(0, len(self.heap) - 1)
        max_value = self.heap.pop()
        self._heapify_down(0)
        return max_value
        
    def _heapify_down(self, index):
        curr_index = max_index = index
        while True:
            left_child = self._left_child(curr_index)
            right_child = self._right_child(curr_index)
            if left_child < len(self.heap) and self.heap[left_child] > self.heap[curr_index]:
                max_index = left_child
            
            if right_child < len(self.heap) and self.heap[right_child] > self.heap[max_index]:
                max_index = right_child
                
            if max_index != curr_index:    
                self._swap(curr_index, max_index)
                curr_index = max_index
            else:
                return
            

def find_kth_smallest(nums, k):
    heap = MaxHeap()
    for i in nums:
        heap.insert(i)
    temp = None
    for i in range(len(nums)-k):
        heap.remove()
    return heap.remove()


def stream_max(nums):
    heap = MaxHeap()
    res = []
    for i in range(len(nums)):
        heap.insert(nums[i])
        res.append(heap.heap[0])
    return res


test_cases = [
    ([], []),
    ([1], [1]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([1, 2, 2, 1, 3, 3, 3, 2, 2], [1, 2, 2, 2, 3, 3, 3, 3, 3]),
    ([-1, -2, -3, -4, -5], [-1, -1, -1, -1, -1])
]

for i, (nums, expected) in enumerate(test_cases):
    result = stream_max(nums)
    print(f'\nTest {i+1}')
    print(f'Input: {nums}')
    print(f'Expected Output: {expected}')
    print(f'Actual Output: {result}')
    if result == expected:
        print('Status: Passed')
    else:
        print('Status: Failed')



"""
    EXPECTED OUTPUT:
    ----------------
    Test 1
    Input: []
    Expected Output: []
    Actual Output: []
    Status: Passed
    Test 2
    Input: [1]
    Expected Output: [1]
    Actual Output: [1]
    Status: Passed
    Test 3
    Input: [1, 2, 3, 4, 5]
    Expected Output: [1, 2, 3, 4, 5]
    Actual Output: [1, 2, 3, 4, 5]
    Status: Passed
    Test 4
    Input: [1, 2, 2, 1, 3, 3, 3, 2, 2]
    Expected Output: [1, 2, 2, 2, 3, 3, 3, 3, 3]
    Actual Output: [1, 2, 2, 2, 3, 3, 3, 3, 3]
    Status: Passed
    Test 5
    Input: [-1, -2, -3, -4, -5]
    Expected Output: [-1, -1, -1, -1, -1]
    Actual Output: [-1, -1, -1, -1, -1]
    Status: Passed

"""

