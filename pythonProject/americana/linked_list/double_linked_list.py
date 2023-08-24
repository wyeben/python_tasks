from americana.linked_list.double_node import DoubleNode


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = DoubleNode(data)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()