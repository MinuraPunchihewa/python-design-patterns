from strategy import IStrategy
from strategy import QuickSortStrategy
from strategy import BubbleSortStrategy
from strategy import SelectionSortStrategy


def sort(items, sort_strategy: IStrategy):
    return sort_strategy.sort(items)


if __name__ == "__main__":
    items = [8, 3, 6, 8, 1, 4, 7, 8, 3, 1]

    # use the Bubble Sort Strategy
    print(sort(items, QuickSortStrategy()))

    # use the Bubble Sort Strategy
    print(sort(items, BubbleSortStrategy()))

    # use the Bubble Sort Strategy
    print(sort(items, SelectionSortStrategy()))