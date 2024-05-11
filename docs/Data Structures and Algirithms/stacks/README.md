# Stacks

## Methods of implementation
A stack in python can be implemented in following ways:
1. [A python list without size limit](stack_list_unlimited.py)
2. [A python list with size limit](stack_list_limited.py)
3. [A linked list](stack_linked_list.py)

## Operations:

* Create Stack
    This creates a new stack.
* Push
    This will add a new element into the stack
* Pop
    This will delete the most recently added element. Stack is always LIFO(Last In First Out)
* Peek
    This will return the latest element added.
* isEmpty
    Checks if there is atleast an element in the stack.
* isFull
    Checks if the stack is full, in case the stack is defined using arrays. In case of python lists, the size is unlimited.
* Delete Stack
    Deletes the entire stack.