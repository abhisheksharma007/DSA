class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
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
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
        
    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.length -= 1
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev  
        return temp
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        if index <0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        
        new_node = Node(value)
        node = self.get(index)
        prev = node.prev
        new_node.prev = prev
        new_node.next = node
        prev.next = new_node
        node.prev = new_node
        self.length += 1
        return True
    
    def remove(self, index):
        if not self.head or index < 0 or index >= self.length:
            return None
        
        if index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        
        node = self.get(index)
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev
        node.prev = None
        node.next = None
        self.length -= 1
        return node
    
    #advance section
    def swap_first_last(self):
        if self.length <= 1:
            return False
        self.head.value, self.tail.value = self.tail.value, self.head.value
        return True
    
    def reverse(self):
        if self.length <= 1:
            return None
        
        temp = self.head
        prev = nxt = None
        while temp:
            nxt = temp.next
            prev = temp.prev
            temp.next = prev
            temp.prev = nxt
            temp = nxt
            
        self.head, self.tail = self.tail, self.head
        return True

    def is_palindrome(self):
        if self.length <= 1:
            return True
        temp = self.head
        hlf = (self.length // 2) if self.length % 2 == 0 else (self.length // 2) + 1
        counter = 1
        check = []
        pop = False
        while temp:
            if counter > hlf:
                if self.length % 2 != 0 and not pop:
                    check.pop()
                    pop = True
                if check.pop() != temp.value:
                    return False
                temp = temp.next
                counter += 1
            else:
                check.append(temp.value)
                temp = temp.next
                counter += 1
        return True

    def swap_pairs(self):
        if self.length <= 1:
            return False
        temp = self.head
        while temp.next:
            if self.head == temp:
                self.head = temp.next
            temp_nxt = temp.next.next
            prev = temp.prev
            nxt = temp.next
            nxt.prev =  prev
            if prev:
                prev.next = nxt
            temp.next = nxt.next
            temp.prev = nxt
            nxt.next = temp
            if temp_nxt:
                temp_nxt.prev = temp
                temp = temp_nxt
        return True


my_dll = DoublyLinkedList(1)
my_dll.append(2)
my_dll.append(3)
my_dll.append(4)
my_dll.append(5)
my_dll.append(6)

print('my_dll before swap_pairs:')
my_dll.print_list()

my_dll.swap_pairs() 


print('my_dll after swap_pairs:')
my_dll.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    my_dll before swap_pairs:
    1 <-> 2 <-> 3 <-> 4
    ------------------------
    my_dll after swap_pairs:
    2 <-> 1 <-> 4 <-> 3

"""