from stack import Stack

# Helper function to determine if a parenthesis is a match
def is_match(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    else:
        return False


def is_paren_balanced(paren_string):
    """This is a stack algorithm that checks if a string of parentheses is balanced.
    It returns True if the string is balanced, and False if it is not.
    
    How does it work?
    1. Create a stack object
    2. Iterate through the string
    3. If the character is an opening parenthesis, push it to the stack
    
    4. If the character is a closing parenthesis, pop the stack and move to next character

    Every closing parenthesis must match the opening parenthesis that precedes it, 
    since we are popping it out of the stack.

    We know that all other characters will now be closing,
     we pop the stack and move to next character until the stack is empty.
    5. If the stack is empty, return True - This means that the string is balanced, as we popped
        all the opening parenthesis out of the stack.

    6. If the stack is not empty, return False - This means that the string is not balanced, as there are
        extra closing/opening parenthesis in the string.
        """
    s = Stack()
    is_balanced = True
    index = 0

    while index < len(paren_string) and is_balanced:
        paren = paren_string[index]
        if paren in "([{":
            s.push(paren)
        else:
            if s.is_empty():
                is_balanced = False
                break
            else:
                top = s.pop()
                if not is_match(top, paren):
                    is_balanced = False
                    break
        index += 1

    if s.is_empty() and is_balanced:
        return True
    else:
        return False

# Tests
print(is_paren_balanced("(["))