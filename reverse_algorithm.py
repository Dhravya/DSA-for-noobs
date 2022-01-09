from stack import Stack

def reverse_string(stack, input_str):
    """This is a stack algorithm that reverses a string.
    
    How does it work?
    1. Create a stack object
    2. Iterate through the string
    3. Push all characters to the stack
    4. Pop all characters from the stack and add them to the output string
    5. Return the output string
    So, Hello becomes this stack:

    O
    l
    l
    E
    H

    and we can simply pop the stack and add it to the output string.

    H E L L O => O L L E H"""

    for i in range(len(input_str)):
        stack.push(input_str[i])
    rev_str = ""
    while not stack.is_empty():
        rev_str += stack.pop()

    return rev_str

# Tests
stack = Stack()
input_str = "!dlroW olleH"
print(reverse_string(stack, input_str))