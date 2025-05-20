import unittest
from main import LinkedList

class TestLinkedListCycle(unittest.TestCase):
    def test_has_cycle(self):
        # Arrange
        ll = LinkedList()
        for val in [3, 2, 0, -4]:
            ll.List_Push(val)

        # Create a cycle at node with value 2
        ll.create_cycle(2)

        # Act
        result = ll.hasCycle()

        # Assert
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()
