class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __str__(self):
        return "{}".format(self.value)

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1   # This attibute is not mandatory, but makes traversal easier through the LL

    def insert(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length = 1

    def __str__(self):

        temp_node = self.head
        result = ""
        while temp_node != None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += " -> "
            temp_node = temp_node.next
        return result
    
    def prepend(self, value):
        
        new_node = Node(value)
        if self.head is not None:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node
        self.length += 1

    def insert(self, value, index):

        if index < 0 or index >self.length:
            print("wrong index value")
            return False
        
        elif index == 0 or self.length == 0:
            self.prepend(value)

        else:
            i = 0
            pointer = self.head
            previous_pointer = None
            for i in range(self.length):
                if i == index - 1:
                    new_node = Node()
                    new_node.next = pointer
                    previous_pointer.next = new_node
                    previous_pointer = pointer
                    pointer = pointer.next

    def append(self, value):

        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1 
            
    def delete(self, index):

        deleted_node = None
        if index < -1 or index > self.length-1:
            return deleted_node
        elif index == 0:
            deleted_node = self.head
            if self.length == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                deleted_node.next = None
            self.length -= 1
        else:
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next

            deleted_node = temp_node.next
            if index == self.length - 1:
                self.tail = deleted_node
            temp_node.next = deleted_node.next
            deleted_node.next = None
            self.length -= 1

        return deleted_node

    def reverse(self):

        prev_node = None
        current_node = self.head

        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head, self.tail = self.tail, self.head

    def middle_node(self):

        slow = self.head
        fast = self.head
        
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def remove_duplicates(self):

        if self.head == None:
            return None

        node_values = set()
        current_node = self.head
        node_values.add(current_node.value)

        while current_node.next:

            if current_node.next.value in node_values:
                current_node.next = current_node.next.next
                self.length -= 1

            else:
                node_values.add(current_node.next.value)
                current_node = current_node.next

        self.tail = current_node

ll = LinkedList(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.append(6)

print(ll)        

print(ll.middle_node())
