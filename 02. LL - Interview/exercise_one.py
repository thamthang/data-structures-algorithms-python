class Node:
    def __init__(self, value):
        """
        Initializes a new instance of the Node class.

        Parameters:
            value (Any): The value to be stored in the node.

        Returns:
            None
        """
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        """
        Initializes a new instance of the LinkedList class
        with a single node containing the given value.

        Parameters:
            value (Any): The value to be stored in the new node.

        Returns:
            None
        """
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

    def append(self, value):
        """
        Add a new node with the given value to the end of the linked list.

        Parameters:
            value (Any): The value to be stored in the new node.

        Returns:
            bool: True if the node is successfully added, False otherwise.
        """
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True

    def find_middle_node(self):
        """
        Find and return the middle node of the linked list.

        Returns:
            The middle node of the linked list.
        """
        slow_pointer = self.head
        fast_pointer = self.head
        while fast_pointer is not None and fast_pointer.next is not None:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

        return slow_pointer

    def has_loop(self):
        """
        A function to check if a linked list has a loop.

        Returns:
            bool: True if the linked list has a loop, False otherwise.
        """
        slow_pointer = self.head
        fast_pointer = self.head
        while fast_pointer is not None and fast_pointer.next is not None:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
            if slow_pointer == fast_pointer:
                return True

        return False


def find_kth_from_end(linked_list, k):
    """
    Find the kth node from the end of the linked list
    given the head node and k.

    Parameters:
        linked_list (LinkedList): The linked list to traverse.
        k (int): The position of the node to find from the end.

    Returns:
        Node: The kth node from the end of the linked list.
        None: If the linked list is empty or None if not found.
    """
    slow_pointer = linked_list.head
    fast_pointer = linked_list.head

    # Move the fast pointer k nodes ahead
    for _ in range(k):
        if fast_pointer is None:
            return None
        fast_pointer = fast_pointer.next

    # Move both pointers until the fast pointer reaches the end
    while fast_pointer is not None:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next

    return slow_pointer
