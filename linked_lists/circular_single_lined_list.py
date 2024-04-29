# Node class for creating each element
class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

# Linked List class to hold all nodes
class CSLinked_List():
    # Initializes an empty Circular Singly Linked List
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0         # This is not required, but helps maintain length of linked list

    # Adds value to the end of the Circular Singly Linked List
    def append(self, value):
        new_node = Node(value)
        # Check if the linked list is empty
        if self.head is None:
            new_node.next = new_node
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1

    # Prints the Circular Singly Linked List
    def __str__(self):
        temp_node = self.head
        result = ""
        while temp_node is not None:
            result += str(temp_node.value)
            temp_node = temp_node.next
            # Check if the next pointer is again at head, last node will point to head
            if temp_node == self.head:
                break
            result += " -> "
        return result

    # Adds a new node at the starting of the circular singly linked list
    def prepend(self, value):
        new_node = Node(value)

        # Check if the linked list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.tail.next = new_node
            self.head = new_node
        
        self.length += 1

    # Insert at a given index in circular linked list
    def insert(self, value, index):

        new_node = Node(value)

        # Calculate the length in case self.length is not available
        length = 0
        temp_node = self.head
        while temp_node.next is not None:
            length += 1
            if temp_node.next == self.head:
                break
            temp_node = temp_node.next

        if index > self.length or index > length:
            raise Exception("Index out of range")

        if index == 0:
            if length == 0 or self.length == 0:
                self.head = new_node
                self.tail = new_node
                new_node.next = new_node
            else:
                new_node.next = self.head
                self.head = new_node
                self.tail.next = new_node
        
        else:
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next

            new_node.next = temp_node.next
            temp_node.next = new_node
            if new_node.next == self.head:           
                self.tail = new_node
        self.length += 1

    # Traverse through the entire circular linked list
    def traverse(self):

        current = self.head

        while current.next is not None:
            print(current.value)
            current = current.next
            if current.next == self.head:
                break

    # Search the circular linked list for a particular value, and return the index
    def search(self, value):

        current = self.head
        index = 0
        while current.next is not None:
            if current.value == value:
                return index
            current = current.next
            index += 1
            if current.next == self.head:
                return False

    # Get the Node at the given index in circular linked list:
    def get(self, index):

        current = self.head
        list_index = 0
        while current.next is not None:
            if index == list_index:
                return current.value
            current = current.next
            list_index += 1
            if current == self.head:
                break
        return False
    
    # Sets/Replaces the value at a particular index
    def set(self, index, value):

        current = self.head

        # Check if index is the head of the circular singly linked list
        if index == 0:
            self.head.value = value
        else:
            pos = 0
            while current.next is not None:
                if index == pos:
                    current.value = value
                    break
                pos += 1
                current = current.next
                if current == self.head:
                    raise Exception("Index out of range")
                
    # Pop/delete the node at the mentioned index, by default deletes the first node
    def pop(self, index = 0):

        temp_node = self.head
        deleted_node = None
        if index < 0:
            raise Exception("Index is negative")
        if index == 0:
            deleted_node = self.head
            self.head = self.head.next
            self.tail.next = self.head
        else:
            pos = 0
            while temp_node.next is not None:
                if index == pos + 1:
                    deleted_node = temp_node.next
                    temp_node.next = deleted_node.next
                    if temp_node.next == self.head:
                        self.tail = temp_node
                    break
                pos += 1
                temp_node = temp_node.next
                if temp_node.next == self.head:
                    raise Exception("Index out of range")

        self.length -= 1
        return deleted_node.value
    
    # Removes the node with the given value from the circular linked list
    def remove(self, value):

        prev_node = self.tail
        temp_node = self.head
        deleted_node = None

        while temp_node.next is not None:

            if temp_node.value == value:
                deleted_node = temp_node
                prev_node.next = deleted_node.next
                deleted_node.next = None
                if deleted_node == self.head:
                    self.head = prev_node.next
                if deleted_node == self.tail:
                    self.tail = prev_node
                break
            prev_node = temp_node
            temp_node = temp_node.next
            if prev_node == self.tail:
                break
        return deleted_node
    
    # Deletes all nodes in the circular singly linked list
    def remove_all(self):
        
        if self.head == None:
            return
        self.tail.next = None
        self.head = None
        self.tail = None
        self.length = 0






ll = CSLinked_List()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.append(6)

print(ll)        
ll.remove_all()
print(ll)