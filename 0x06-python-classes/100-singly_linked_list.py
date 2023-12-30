#!/usr/bin/python3

'''task 100'''


class Node:
    '''task 100'''

    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """Getter method to retrieve the data."""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter method to set the data."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """Getter method to retrieve the next_node."""
        if self.__next_node is not None:
            return self.__next_node
        else:
            return None

    @next_node.setter
    def next_node(self, value):
        """Setter method to set the next_node."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


''' this class make linkedlist'''


class SinglyLinkedList:
    '''make linkedlist'''

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node into the correct sorted position in the list."""
        new_node = Node(value)

        if not self.__head or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        current = self.__head
        while current.next_node and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """Print the entire list in stdout, one node number by line."""
        result = ""
        current = self.__head
        while current:
            result += str(current.data) + ("\n" if current.next_node else "")
            current = current.next_node
        return result


'''
# test case:

sll = SinglyLinkedList()
sll.sorted_insert(2)
sll.sorted_insert(5)
sll.sorted_insert(3)
sll.sorted_insert(10)
sll.sorted_insert(1)
sll.sorted_insert(-4)
sll.sorted_insert(-3)
sll.sorted_insert(4)
sll.sorted_insert(5)
sll.sorted_insert(12)
sll.sorted_insert(3)
print(sll)
'''
