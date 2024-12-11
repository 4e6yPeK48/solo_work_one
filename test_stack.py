import unittest
from stack import Stack


class TestStack(unittest.TestCase):
    """
    Класс TestStack содержит тесты для проверки функциональности класса Stack.

    :ivar stack: The stack to be tested.
    :vartype stack: Stack
    """

    def test_push_pop(self) -> None:
        """
        Тестирует методы push и pop.
        """
        stack = Stack()
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)
        with self.assertRaises(IndexError):
            stack.pop()

    def test_peek(self) -> None:
        """
        Тестирует метод peek.
        """
        stack = Stack()
        stack.push(1)
        self.assertEqual(stack.peek(), 1)
        stack.push(2)
        self.assertEqual(stack.peek(), 2)
        stack.pop()
        self.assertEqual(stack.peek(), 1)

    def test_is_empty(self) -> None:
        """
        Тестирует метод is_empty.
        """
        stack = Stack()
        self.assertTrue(stack.is_empty())
        stack.push(1)
        self.assertFalse(stack.is_empty())

    def test_clear(self) -> None:
        """
        Тестирует метод clear.
        """
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.clear()
        self.assertTrue(stack.is_empty())

    def test_print(self) -> None:
        """
        Тестирует метод __str__.
        """
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(str(stack), '3 -> 2 -> 1')


if __name__ == "__main__":
    unittest.main()
