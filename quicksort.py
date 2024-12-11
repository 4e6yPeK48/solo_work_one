from stack import Stack


def hoare_partition(stack: Stack, low: int, high: int) -> int:
    """
    Разбивает стек на две части относительно опорного элемента.

    :param stack: Стек, который нужно разбить.
    :type stack: Stack
    :param low: Нижняя граница разбиения.
    :type low: int
    :param high: Верхняя граница разбиения.
    :type high: int
    :return: Индекс опорного элемента.
    :rtype: int
    """
    pivot = stack.peek_at(low)
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while stack.peek_at(i) < pivot:
            i += 1
        j -= 1
        while stack.peek_at(j) > pivot:
            j -= 1
        if i >= j:
            return j
        stack.swap(i, j)


def quicksort(stack: Stack, low: int, high: int) -> None:
    """
    Сортирует стек в порядке возрастания.

    :param stack: Стек, который нужно отсортировать.
    :type stack: Stack
    :param low: Нижняя граница сортировки.
    :type low: int
    :param high: Верхняя граница сортировки.
    :type high: int
    """
    if low < high:
        p = hoare_partition(stack, low, high)
        quicksort(stack, low, p)
        quicksort(stack, p + 1, high)


def sort_stack(stack: Stack) -> None:
    """
    Сортирует стек в порядке возрастания.

    :param stack: Стек, который нужно отсортировать.
    :type stack: Stack
    """
    if not stack.is_empty():
        quicksort(stack, 0, stack.size() - 1)
