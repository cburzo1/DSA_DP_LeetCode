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

    def create_cycle(self, n):
        current = self.head
        current2 = self.head

        while current.next is not None:
            current = current.next

        while current2.val != n:
            current2 = current2.next

        print(current.next)

        if current.next is None:
            print("none?")
            current.next = current2

        print(current.next)
        print(current.val)

    def List_Traverse(self):
        current = self.head

        while current != None:
            print(current.val)
            current = current.next

        print(current)

    def hasCycle(self):
        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

List1 = LinkedList()

List1.List_Push(3)
List1.List_Push(2)
List1.List_Push(0)
List1.List_Push(-4)

#List1.create_cycle(2)

print(List1.hasCycle())

#List1.List_Traverse()