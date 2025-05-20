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

        while current is not None:
            print(current.val)
            current = current.next

    def reverseList(self, head):
        left = head
        middle = head.next
        right = head.next.next
        print(left.val, middle.val, right.val)

        left.next = None
        print(left.val, middle.val, right.val, right.next.val)
        print(left.next, middle.next.val)
        middle.next = left
        print(left.next, middle.next.val)
        left = middle
        print(left.next.val, middle.val)

        head = middle

        List1.List_Traverse()

List1 = LinkedList()

List1.List_Push(1)
List1.List_Push(2)
List1.List_Push(3)
List1.List_Push(4)
List1.List_Push(5)

List1.reverseList(List1.head)

#List1.List_Traverse()