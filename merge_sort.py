


def merge(list1, list2):
    combined = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i += 1
        else:
            combined.append(list2[j])
            j += 1
    while i < len(list1):
        combined.append(list1[i])
        i += 1
    while j < len(list2):
        combined.append(list2[j])
        j += 1
        
    return combined

def merge_sort(original_list):
    if len(original_list) == 1:
        return original_list
    
    mid = len(original_list)//2
    left = merge_sort(original_list[:mid])
    right = merge_sort(original_list[mid:])
    
    return merge(left, right)




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

    def merge(self, other_list):
        curr = self.head
        dummy_list = LinkedList(0)
        ol = other_list.head
        while curr and ol:
            if curr.value < ol.value:
                dummy_list.append(curr.value)
                curr = curr.next
            else:
                dummy_list.append(ol.value)
                ol = ol.next
        while curr:
            dummy_list.append(curr.value)
            curr = curr.next
        while ol:
            dummy_list.append(ol.value)
            ol = ol.next
        self.head = dummy_list.head.next
        self.tail = dummy_list.tail
        self.length = dummy_list.length-1
        return True

    def merge(self, other_list):
        curr = self.head
        ol = other_list.head
        length = 0
        dummy_node = Node(0)
        dummy_head = dummy_node
        while curr and ol:
            if curr.value < ol.value:
                dummy_node.next = curr
                curr = curr.next
            else:
                dummy_node.next = ol
                ol = ol.next
            dummy_node = dummy_node.next
            length += 1
            self.tail = dummy_node
        while curr:
            dummy_node.next = curr
            dummy_node = dummy_node.next
            self.tail = dummy_node
            length += 1
            curr = curr.next
        while ol:
            dummy_node.next = ol
            dummy_node = dummy_node.next
            self.tail = dummy_node
            length += 1
            ol = ol.next
        self.head = dummy_head.next
        self.length = length
        return True


l1 = LinkedList(1)
l1.append(3)
l1.append(5)
l1.append(7)


l2 = LinkedList(2)
l2.append(4)
l2.append(6)
l2.append(8)

l1.merge(l2)

l1.print_list()

"""
    EXPECTED OUTPUT:
    ----------------
    1 
    2 
    3 
    4 
    5 
    6 
    7
    8

"""