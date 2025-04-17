class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None

    def List_Push(self, data):
        newNode = Node(data)

        if self.head == None:
            self.head = newNode

        else:
            current = self.head

            while current.next != None:
                current = current.next

            current.next = newNode

    def List_Traverse(self):
        current = self.head

        while current != None:
            print(current.val)
            current = current.next

List1 = LinkedList()

List1.List_Push(5)
List1.List_Push(6)
List1.List_Push(4)
List1.List_Push(9)

List1.List_Traverse()