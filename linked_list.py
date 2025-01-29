class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1
        return True
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next    
            
    def make_empty(self):
        self.head = None
        self.length = 0
        
    def find_middle_node(self):
        slow = fast = self.head
        if not slow.next:
            return slow
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def has_loop(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    
    def find_kth_from_end(linked_list, k):
        slow = fast = linked_list.head
        counter = k
        while fast:
            if counter <= 0:
                slow = slow.next
            fast = fast.next
            counter -= 1
        if counter > 0:
            return None
        return slow
    
    def partition_list(self, value):
        temp = self.head
        less = more = more_head = None
        while temp:
            if temp.value < value:
                if not less:
                    less = Node(temp.value)
                    self.head = less
                else:
                    less.next = Node(temp.value)
                    less = less.next
            else:
                if not more:
                    more = Node(temp.value)
                    more_head = more
                else:
                    more.next = Node(temp.value)
                    more = more.next
            temp = temp.next
        if less:
            less.next = more_head
        else:
            self.head = more_head
            
    def remove_duplicates(self):
        dups = set()
        pre = next = None
        temp = self.head
        while temp:
            next = temp.next
            if temp.value in dups:
                if pre: pre.next = next
                temp.next = None
                temp = pre
                self.length -= 1
            else:
                dups.add(temp.value)
            pre = temp
            temp = next
            
    def binary_to_decimal(self):
        temp = self.head
        dec = 0
        counter = self.length - 1
        while temp:
            dec += 2**counter * temp.value
            temp = temp.next
            counter -= 1
        return dec

    def reverse_between(self, start, end):
        if self.length <= 1 or start == end or start >= self.length or end >= self.length:
            return None
        
        current = self.head
        counter = 0
        ss_head = self.head
        ss_headprev = None
        while current:
            if counter == start-1:
                ss_headprev = current
                ss_head = current.next
            elif counter == end:
                ss_tail = current
                ss_tailnext = current.next
                break
            current = current.next
            counter += 1
        
        current = ss_head
        prev = nxt = None
        while current and current != ss_tailnext:
            nxt = current.next
            current.next = prev
            prev = current                
            current  = nxt
            
        if ss_headprev:
            ss_headprev.next = prev
        else:
            self.head = prev

        ss_head.next = ss_tailnext



linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

print("Original linked list: ")
linked_list.print_list()

# Reverse a sublist within the linked list
linked_list.reverse_between(2, 4)
print("Reversed sublist (2, 4): ")
linked_list.print_list()

# Reverse another sublist within the linked list
linked_list.reverse_between(0, 4)
print("Reversed entire linked list: ")
linked_list.print_list()

# Reverse a sublist of length 1 within the linked list
linked_list.reverse_between(3, 3)
print("Reversed sublist of length 1 (3, 3): ")
linked_list.print_list()

# Reverse an empty linked list
empty_list = LinkedList(0)
empty_list.make_empty
empty_list.reverse_between(0, 0)
print("Reversed empty linked list: ")
empty_list.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    Original linked list: 
    1
    2
    3
    4
    5
    Reversed sublist (2, 4): 
    1
    2
    5
    4
    3
    Reversed entire linked list: 
    3
    4
    5
    2
    1
    Reversed sublist of length 1 (3, 3): 
    3
    4
    5
    2
    1
    Reversed empty linked list: 
    None
    
"""
