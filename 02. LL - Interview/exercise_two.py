class Node:
    def __init__(self, value):
        """
        Initializes a new instance of the Node class.

        Args:
            value (Any): The value to be stored in the node.

        Attributes:
            value (Any): The value stored in the node.
            next (Node or None): The next node in the linked list
                or None if there is no next node.
        """
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        """
        Initializes a new instance of the LinkedList class.

        Args:
            value (Any): The value to be stored in the new node.

        Initializes the LinkedList with a single node containing
        the given value.
        Set the head of the LinkedList to the newly created node.
        Set the length of the LinkedList to 1.
        """
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        """
        Appends a new node with the given value to the end of the linked list.

        Parameters:
            value (Any): The value to be stored in the new node.

        Returns:
            None
        """
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
        self.length += 1

    def print_list(self):
        """
        Print the values of all nodes in the linked list.

        This method iterates through the linked list starting from the head
        node and prints the value of each node.

        Parameters:
            None

        Returns:
            None
        """
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def make_empty(self):
        """
        Reset the linked list.
        """
        self.head = None
        self.tail = None
        self.length = 0

    def partition_list(self, x):
        """"
        Partition the linked list based on the given value x.

        Parameters:
            x (Any): The value to partition the list on.

        Returns:
            None
        """
        if self.head is None:
            return None

        dummy1 = Node(0)
        dummy2 = Node(0)
        prev1 = dummy1
        prev2 = dummy2
        current = self.head

        while current:
            if current.value < x:
                prev1.next = current
                prev1 = current
            else:
                prev2.next = current
                prev2 = current
            current = current.next

        prev1.next = None
        prev2.next = None
        prev1.next = dummy2.next

        self.head = dummy1.next
