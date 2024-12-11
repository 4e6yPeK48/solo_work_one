import unittest
from stack import Stack
from quicksort import sort_stack


class TestStackSorting(unittest.TestCase):
    """
    Класс TestStackSorting содержит тесты для проверки функции sort_stack.

    :ivar stack: Стек, который будет тестироваться.
    :vartype stack: Stack
    """

    def test_sort_stack(self) -> None:
        """
        Тестирует функцию sort_stack.
        """
        stack = Stack()
        values = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        for value in values:
            stack.push(value)
        sort_stack(stack)
        sorted_values = sorted(values)
        for value in sorted_values:
            self.assertEqual(stack.pop(), value)


if __name__ == "__main__":
    unittest.main()
