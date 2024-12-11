class Node:
    """
    Класс Node представляет узел в связном списке.

    :ivar value: Значение узла.
    :vartype value: int
    :ivar next_node: Ссылка на следующий узел.
    :vartype next_node: Node
    """

    def __init__(self, value: int, next_node: 'Node' = None) -> None:
        """
        Инициализирует узел с заданным значением и ссылкой на следующий узел.

        :param value: Значение узла.
        :type value: int
        :param next_node: Ссылка на следующий узел.
        :type next_node: Node, опционально
        """
        self.value = value
        self.next_node = next_node
