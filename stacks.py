class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
        
   
class Stack():
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1
        
    def push(self, value):
        new_node = Node(value)
        if not self.top:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
            
        self.height += 1
        return True
    
    def pop(self):
        if self.height == 0:
            return None
        temp = self.top
        if self.height == 1:
            self.top = None
        else:
            self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp
    
    
# my_stack = Stack(2)

# print('Stack before push(1):')
# my_stack.print_stack()

# my_stack.push(1)

# print('\nStack after push(1):')
# my_stack.print_stack()



"""
    EXPECTED OUTPUT:
    ----------------
    Stack before push(1):
    2

    Stack after push(1):
    1
    2   

"""

    
    
#advance
class StackList():
    def __init__(self):
        self.stack_list = []
        
    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop (self):
        if self.is_empty():
            return None
        return self.stack_list.pop()     
   
 
def sort_stack(stack):
    temp_stack = StackList()
    while not stack.is_empty():
        temp = stack.pop()
        while not temp_stack.is_empty() and temp < temp_stack.peek():
            stack.push(temp_stack.pop())
        temp_stack.push(temp)
        
    while not temp_stack.is_empty():
        stack.push(temp_stack.pop())


my_stack = StackList()
my_stack.push(3)
my_stack.push(1)
my_stack.push(5)
my_stack.push(4)
my_stack.push(2)

print("Stack before sort_stack():")
my_stack.print_stack()

sort_stack(my_stack)

print("\nStack after sort_stack:")
my_stack.print_stack()

    
    
    
def reverse_string(string):
    if not string:
        return ''
    if len(string) == 1:
        return string
    stack = StackList()
    for i in string:
        stack.push(i)
    return ''.join([stack.pop() for _ in range(stack.size())])

my_string = 'hello'
# print ( reverse_string(my_string) )
"""
    EXPECTED OUTPUT:
    ----------------
    olleh

"""


def is_balanced_parentheses(string):
    stack = StackList()
    hlf = len(string) // 2
    counter = 0
    while counter < len(string):
        if string[counter] == '(':
            stack.push(string[counter])
        else:
            if stack.is_empty(): return False
            stack.pop()
        counter += 1

    if not stack.is_empty():
        return False
    return True

def test_is_balanced_parentheses():
    try:
        assert is_balanced_parentheses('((()))') == True
        print('Test case 1 passed')
    except AssertionError:
        print('Test case 1 failed')

    try:
        assert is_balanced_parentheses('()') == True
        print('Test case 2 passed')
    except AssertionError:
        print('Test case 2 failed')

    try:
        assert is_balanced_parentheses('(()())') == True
        print('Test case 3 passed')
    except AssertionError:
        print('Test case 3 failed')

    try:
        assert is_balanced_parentheses('(()') == False
        print('Test case 4 passed')
    except AssertionError:
        print('Test case 4 failed')

    try:
        assert is_balanced_parentheses('())') == False
        print('Test case 5 passed')
    except AssertionError:
        print('Test case 5 failed')

    try:
        assert is_balanced_parentheses(')(') == False
        print('Test case 6 passed')
    except AssertionError:
        print('Test case 6 failed')

    try:
        assert is_balanced_parentheses('') == True
        print('Test case 7 passed')
    except AssertionError:
        print('Test case 7 failed')

    try:
        assert is_balanced_parentheses('()()()()') == True
        print('Test case 8 passed')
    except AssertionError:
        print('Test case 8 failed')

    try:
        assert is_balanced_parentheses('(())(())') == True
        print('Test case 9 passed')
    except AssertionError:
        print('Test case 9 failed')

    try:
        assert is_balanced_parentheses('(()()())') == True
        print('Test case 10 passed')
    except AssertionError:
        print('Test case 10 failed')

    try:
        assert is_balanced_parentheses('((())') == False
        print('Test case 11 passed')
    except AssertionError:
        print('Test case 11 failed')

# test_is_balanced_parentheses()