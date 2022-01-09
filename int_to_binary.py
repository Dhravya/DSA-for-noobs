from stack import Stack
import math


def convert_int_to_bin(dec_num):
    """Convert an integer to binary.

    How does it work?
    
    Its important to know how the logic of converting int to binary works.
    The logic is simple:
    - If the number is 0, return 0
    - If the number is 1, return 1
    - If the number is greater than 1, divide the number by 2 and add the remainder to the stack 
        The quotient obtained from the division is used to determine the next bit.
    - Repeat the process until the number is 0.

    So, Lets say we have the number:
    - 5
    - 5 / 2 = 2 with remainder 1
    - 2 / 2 = 1 with remainder 0
    - 1 / 2 = 0 with remainder 1

    So, the stack will look like this:
    - 1
    - 0
    - 1

    So, the binary representation of 5 is:
    - 1
    - 0
    - 1
    (Its the reverse of the stack obtained)

    Put another way, all the remainders are added to the stack, and quotients 
        are used to determine the next bit.
    after the stack is made, the stack is reversed and the binary representation is returned.

    To have a better understanding, change `n` below to any number and run the program.
    """

    stack = Stack()
    print("___________________________")
    while True:
        quotient = dec_num // 2
        remainder = dec_num % 2
        stack.push(remainder)
        dec_num = quotient
        string = "|Quotient: "+ str(quotient)+ " Remainder: "+ str(remainder)
        al = " "*(27-len(string)) + "|"
        print(string +al)
        if quotient == 0:
            break
    print("____________________________")
    print("Now, we will reverse the stack and obtain the binary representation of the number.")
    bin_num = ""
    while not stack.is_empty():
        bin_num += str(stack.pop())
    return bin_num

n = 5
ans = convert_int_to_bin(n)
print(f"\nCalculated Value: {ans} ; Expected Value: {bin(n)[2:]} \n       Correct answer? { ans== bin(n)[2:]}")