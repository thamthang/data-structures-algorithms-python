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
        self.length = 1

    def print_list(self):
        """
        Print the values of all nodes in the linked list.
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

        self.length += 1

        return True

    def pop(self):
        """
        Remove and return the last node from the linked list.

        Returns:
            Node: The removed node.
            None: If the linked list is empty.
        """
        popped_node = None
        if self.length > 0:
            if self.length == 1:
                popped_node = self.head
                self.head = None
                self.tail = None
                self.length = 0
            else:
                temp = self.head
                while temp is not None:
                    if temp.next == self.tail:
                        popped_node = self.tail
                        temp.next = None
                        self.tail = temp
                        self.length -= 1
                        break
                    temp = temp.next
        return popped_node

    def prepend(self, value):
        """
        Add a new node with the given value to the beginning of
        the linked list.

        Parameters:
            value (Any): The value to be stored in the new node.

        Returns:
            bool: True if the node is successfully prepended, False otherwise.
        """
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.length += 1

        return True

    def pop_first(self):
        """
        Remove and return the first node from the linked list.

        Returns:
            Node: The removed node.
            None: If the linked list is empty.
        """
        if self.length == 0:
            return None

        popped_node = self.head
        self.head = self.head.next
        popped_node.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None

        return popped_node

    def get(self, index):
        """
        Returns the node at the specified index in the linked list.

        Parameters:
            index (int): The index of the node to retrieve.

        Returns:
            Node: The node at the specified index.
            None: if the index is out of bounds.
        """
        if index < 0 or self.length == 0 or self.length < index:
            return None

        temp = self.head
        for _ in range(index):
            temp = temp.next

        return temp

    def set_value(self, index, value):
        """
        Sets the value of the node at the specified index to the given value.

        Parameters:
            index (int): The index of the node to be updated.
            value (Any): The new value to be set.

        Returns:
            bool: True if the value was successfully set, False otherwise.
        """
        temp = self.get(index)
        if temp is not None:
            temp.value = value
            return True

        return False

    def insert(self, index, value):
        """
        Inserts a new node with the given value at the specified index
        in the linked list.

        Parameters:
            index (int): The index at which the new node should be inserted.
            value: The value to be stored in the new node.

        Returns:
            bool: True if the node is successfully inserted, False otherwise.
        """
        if index < 0 or index > self.length:
            return False

        if index == 0:
            return self.prepend(value)

        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        current_node = self.get(index)
        if current_node:
            new_node.next = current_node
        previous_node = self.get(index - 1)
        if previous_node:
            previous_node.next = new_node

        self.length += 1
        return True

    def remove(self, index):
        """
        Removes the node at the specified index from the linked list.

        Parameters:
            index (int): The index of the node to be removed.

        Returns:
            Node: The removed node.
            None: if the index is out of bounds.
        """
        if index < 0 or index > self.length:
            return None

        if index == 0:
            return self.pop_first()

        if index == (self.length - 1):
            return self.pop()

        current_node = self.get(index)
        pre_node = self.get(index - 1)

        if (current_node and pre_node):
            pre_node.next = current_node.next
            self.length -= 1
            return current_node

        return None

    def reverse(self):
        """
        Reverses the order of the linked list.

        This function reverses the order of the linked list.

        Parameters:
            self (LinkedList): The linked list object.

        Returns:
            None
        """
        temp = self.head
        self.head = self.tail
        self.tail = temp

        before = None
        while temp is not None:
            after = temp.next
            temp.next = before
            before = temp
            temp = after
