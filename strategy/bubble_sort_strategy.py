from strategy import IStrategy


class BubbleSortStrategy(IStrategy):
    def sort(self, items):
        sorted = False

        while not sorted:
            sorted = True
            for i in range(0, len(items) - 1):
                if items[i + 1] < items[i]:
                    sorted = False
                    items[i], items[i + 1] = items[i + 1], items[i]

        return items
    