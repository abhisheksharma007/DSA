def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr), 1):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr



def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


# O(n) for almost sorted list
def insertion_sort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i-1
        while arr[j] > temp and j > -1:
            arr[j+1] = arr[j]
            arr[j] = temp
            j -= 1
    return arr

 
 
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def bubble_sort(self):
        if self.length < 2:
            return
        temp = self.head
        while temp:
            new_temp = temp.next
            while new_temp:
                if new_temp.value < temp.value:
                    temp.value, new_temp.value = new_temp.value, temp.value
                new_temp = new_temp.next
            temp = temp.next
        return True
    
    
    def selection_sort(self):
        if self.length < 2:
            return
        temp = self.head
        while temp:
            min_node = temp
            new_temp = temp.next
            while new_temp:
                if new_temp.value < min_node.value:
                    min_node = new_temp
                new_temp = new_temp.next
            if min_node != temp:
                temp.value, min_node.value = min_node.value, temp.value
            temp = temp.next
        return True
    
    def insertion_sort_swap_values(self):
        if self.length < 2:
            return None
        temp = self.head.next
        while temp:
            new_temp = self.head
            while new_temp.next != temp:
                if temp.value < new_temp.value:
                    temp.value, new_temp.value = new_temp.value, temp.value
                new_temp = new_temp.next      
            temp = temp.next
        return True
    
    def insertion_sort_swap_nodes(self):
        if self.length < 2:
            return None
        
        sorted_head = self.head
        current = self.head.next
        sorted_head.next = None
        
        while current:
            next_node = current.next
            if current.value < sorted_head.value:
                current.next = sorted_head
                sorted_head = current
            else:
                search = sorted_head
                while search.next and search.next.value < current.value:
                    search = search.next
                current.next = search.next
                search.next = current
            current = next_node

        self.head = sorted_head
        return True

    
    
my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(6)
my_linked_list.append(5)
my_linked_list.append(1)
my_linked_list.append(3)

print("Linked List Before Sort:")
my_linked_list.print_list()

my_linked_list.insertion_sort_swap_nodes()

print("\nSorted Linked List:")
my_linked_list.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    Linked List Before Sort:
    4
    2
    6
    5
    1
    3

    Sorted Linked List:
    1
    2
    3
    4
    5
    6

"""

