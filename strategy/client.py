from strategy.bubble_sort_strategy import BubbleSortStrategy
from strategy.quick_sort_strategy import QuickSortStrategy


if __name__ == "__main__":
    inputs = [8, 3, 6, 8, 1, 4, 7, 8, 3, 1]
    sorted_list = QuickSortStrategy().sort(inputs)
    print(sorted_list)