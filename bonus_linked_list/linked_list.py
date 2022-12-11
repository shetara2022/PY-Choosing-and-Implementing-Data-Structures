# Write code for implementing a linked list below

class Node:
    def __init__(self, data, reference=None):
        self.data = data
        self.reference = reference 

class Linked_List:
    def __init__(self, head = None):
        self.head = head


list1 = Linked_List()
list1.self.head = Node("January")
lst2 = Node("February")

list1.head.reference = lst2