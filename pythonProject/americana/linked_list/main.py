from americana.linked_list.double_linked_list import DoubleLinkedList
from americana.linked_list.singly_linked_list import SinglyLinkedList

list = SinglyLinkedList()
list.insert(18)
list.insert(35)
list.insert(16)

print("Singly linked list:")
list.display()

list2 = DoubleLinkedList()
list2.insert(78)
list2.insert(42)
list2.insert(15)

print("Double linked list:")
list2.display()