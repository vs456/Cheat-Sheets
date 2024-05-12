# Queues

## Basic Introduction:

## Methods of implementation
A queue in python can be implemented in following ways:
1. [A python list without size limit](queue_list_unlimited.py)
2. [A circular queue as a python list, limited size](circular_queue.py)
3. [A linked list](queue_linked_list.py)
4. [Using collections.deque Class](https://docs.python.org/3/library/collections.html#deque-objects). Operations supported include:
    * deque(): Creates a new queue
    * append(): Appends an element at the end
    * popleft(): Deletes the left most element
    * clear(): Clears the entire queue
5. [Using python queue module](https://docs.python.org/3/library/queue.html). Supports both FIFO and LIFO queues. Operations include:
    * qsize(): Return the size of the queue
    * empty(): Checks if the queue is empty or not
    * full(): Checks if the queue is full
    * put(): Adds an element to the end of queue
    * get(): Removes the first element from the queue
    * task_done(): Indicate that a formerly enqueued task is complete
    * join(): Blocks the queue till all operations have been completed and task_done method has been called for them
6. [Using multiprocessing module]()

## Operations:

* Create Queue
    This creates a new stack.
* Enqueu
    This will add a new element into the queue.
* Dequeue
    This will delete the first added element. Queue is always FIFO(First In First Out).
* Peek
    This will return the first element added.
* isEmpty
    Checks if there is atleast an element in the queue.
* isFull
    Checks if the stack is full, in case the stack is defined using arrays. In case of python lists, the size is unlimited.
* Delete Queue
    Deletes the entire queue.