# Data Structures and Algorithms:

This is a collection of data structures and algorithms that I write while learning the subject

## Stack:
stack.py
A stack algorithm is a data structure that is like a pack of cards - a stack.
Stack has the following properties:

### Push
Adds element to the top of the stack

### Pop
Removes element from the top of the stack

### Peek
Returns the element at the top of the stack

Size and is_empty are just helper functions 

### Stuff Done with stack:
- Checking if a bracket string is balanced
    Explanation:
    - Add all brackets in the stack one by one
    - on reaching a closing bracket, check if the top of the stack is a matching bracket
    - if it is, pop the top of the stack and check the next bracket
    - rinse and repeat 
    - if the stack is empty, the string is balanced
    - otherwise, the string is not balanced in the end

- Reverse algorithm
    Explanation:
    - Add all characters in the string to the stack
    - make a new string - which will hold the return value
    - pop the top of the stack until its empty and add it to the string
    - Voila! the string has been reversed

- Int to binary conversion
    Explanation:
    - Divide the integer by 2 and add the remainder to the stack
    - the quotient obtained from the division is what we'll use to get the next remainder
    - Keep repeating until the quotient is 0
    - Reverse the stack by popping its values to obtain the binary string
    ```
        ___________________________
        |Quotient: 2 Remainder: 1  | - remainder added (Current stack: 1)
        |Quotient: 1 Remainder: 0  | - remainder added (Current stack: 10)
        |Quotient: 0 Remainder: 1  | - remainder added (Current stack: 101)
        ____________________________
        Answer will be the reverse of this stack : 101
        ```
