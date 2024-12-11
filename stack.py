from node import Node


class Stack:
    """
    Представляет структуру данных стек, используя связный список.

    :ivar head: Верхний узел стека.
    :vartype head: Node
    """

    def __init__(self) -> None:
        """
        Инициализирует пустой стек.
        """
        self.head = None

    def is_empty(self) -> bool:
        """
        Проверяет, пуст ли стек.

        :return: True, если стек пуст, иначе False.
        :rtype: bool
        """
        return self.head is None

    def push(self, value: int) -> None:
        """
        Добавляет значение в стек.

        :param value: Значение, которое нужно добавить в стек.
        :type value: int
        """
        new_node = Node(value, self.head)
        self.head = new_node

    def pop(self) -> int:
        """
        Удаляет и возвращает верхнее значение из стека.

        :raises IndexError: Если стек пуст.
        :return: Значение на вершине стека.
        :rtype: int
        """
        if self.is_empty():
            raise IndexError('pop из пустого стека')
        value = self.head.value
        self.head = self.head.next_node
        return value

    def peek(self) -> int:
        """
        Возвращает верхнее значение, не удаляя его.

        :raises IndexError: Если стек пуст.
        :return: Значение на вершине стека.
        :rtype: int
        """
        if self.is_empty():
            raise IndexError('peek из пустого стека')
        return self.head.value

    def clear(self) -> None:
        """
        Удаляет все элементы из стека.
        """
        self.head = None

    def size(self) -> int:
        """
        Возвращает размер стека.

        :return: Размер стека.
        :rtype: int
        """
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next_node
        return count

    def peek_at(self, index: int) -> int:
        """
        Возвращает значение на заданной позиции в стеке.

        :param index: Позиция в стеке.
        :type index: int
        :raises IndexError: Если индекс вне диапазона.
        :return: Значение на заданной позиции.
        :rtype: int
        """
        current = self.head
        for _ in range(index):
            if current is None:
                raise IndexError('Индекс вне диапазона')
            current = current.next_node
        if current is None:
            raise IndexError('Индекс вне диапазона')
        return current.value

    def swap(self, i: int, j: int) -> None:
        """
        Меняет местами значения на позициях i и j в стеке.

        :param i: Первая позиция.
        :type i: int
        :param j: Вторая позиция.
        :type j: int
        :raises IndexError: Если один из индексов вне диапазона.
        """
        if i == j:
            return
        current_i = self.head
        current_j = self.head
        for _ in range(i):
            if current_i is None:
                raise IndexError('Индекс i вне диапазона')
            current_i = current_i.next_node
        for _ in range(j):
            if current_j is None:
                raise IndexError('Индекс j вне диапазона')
            current_j = current_j.next_node
        if current_i is None or current_j is None:
            raise IndexError('Индекс вне диапазона')
        current_i.value, current_j.value = current_j.value, current_i.value

    def __str__(self) -> str:
        """
        Возвращает строковое представление стека.

        :return: Строковое представление стека.
        :rtype: str
        """
        result = []
        current = self.head
        while current is not None:
            result.append(str(current.value))
            current = current.next_node
        return " -> ".join(result)

    def __repr__(self) -> str:
        """
        Возвращает строковое представление стека для отладки.

        :return: Строковое представление стека для отладки.
        :rtype: str
        """
        return f'Stack({str(self)})'
