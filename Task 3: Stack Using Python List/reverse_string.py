# Import the Stack class from the stack implementation file
from StackClassImplementation import Stack

# Function to reverse a string using a stack
def reverse_string(s):
    stack = Stack()
    
    # Push each character of the string into the stack
    for char in s:
        stack.push(char)

    # Pop characters to get them in reverse order
    reversed_str = ''
    while not stack.is_empty():
        reversed_str += stack.pop()
    
    return reversed_str

# Test the function
original = "Anubhav"
print("Original:", original)
print("Reversed:", reverse_string(original))
