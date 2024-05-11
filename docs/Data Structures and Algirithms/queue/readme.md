# Queues

## Basic Introduction:

## Methods of implementation
A queue in python can be implemented in following ways:
1. [A python list without size limit](queue_list_unlimited.py)
2. [A circular queue as a python list, limited size](circular_queue_list.py)
3. [A linked list](stack_linked_list.py)

## Operations:

* Create Queue
    This creates a new stack, in python it can be created using:
    * [A python list without size limit](stack_list_unlimited.py)
    * [A python list with size limit](stack_list_limited.py)
    * [A linked list](stack_linked_list.py)
* Enqueu
    This will add a new element into the queue.
* Dequeue
    This will delete the first added element. Queue is always FIFO(First In First Out).
* Peek
    This will return the latest element added.
* isEmpty
    Checks if there is atleast an element in the stack.
* isFull
    Checks if the stack is full, in case the stack is defined using arrays. In case of python lists, the size is unlimited.
* Delete Queue
    Deletes the entire stack.