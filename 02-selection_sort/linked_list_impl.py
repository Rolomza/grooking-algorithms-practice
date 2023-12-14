class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        '''
        Adds an element at the end of the list
        '''
        new_node = Node(data)
        if not self.head:
            # If the list is empty, both head and tail point to the new node
            self.head = new_node
            self.tail = new_node
        else:
            # Otherwise, add the new node to the end and update the tail
            self.tail.next = new_node
            self.tail = new_node

    def index(self, data):
        '''
        Returns the lowest index where the element appears. 
        '''
        actual_index = 0
        current = self.head
        while current:
            if current.data == data:
                return actual_index
            actual_index += 1
            current = current.next
        return None
    
    
    def insert(self, index, data):
        '''
        Inserts a given element at a given index in a list.
        '''
        if (index > self.length() - 1) or index < 0:
            return "Index error"

        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return None
        
        if index == 0:
            new_node.next = current
            self.head = new_node
            return
        
        prev = self.head
        current = self.head.next
        actual_index = 1

        while current:

            if index == actual_index:
                new_node.next = current
                prev.next = new_node
                return None

            actual_index += 1
            prev = current
            current = current.next
        
    def remove(self, data):
        '''
        Removes a given object from the List.
        '''

        if self.head.data == data:
            self.head = self.head.next
            return
        
        prev = self.head
        current = self.head.next
        actual_index = 1

        while current:
            if current.data == data:
                prev.next = current.next
                current.next = None
                return None

            actual_index += 1
            prev = current
            current = current.next


    def length(self):
        '''
        Calculates the total length of the List.
        '''
        total_nodes = 0
        current = self.head
        while current:
            total_nodes += 1
            current = current.next

        return total_nodes

    
    def print_list(self):
        '''
        Show the elements of the list.
        '''
        current = self.head
        print("[", end="")
        while current:
            print(current.data, end=" ")
            current = current.next
        print("]")