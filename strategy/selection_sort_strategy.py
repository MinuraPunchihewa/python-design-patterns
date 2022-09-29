from strategy import IStrategy


class SelectionSortStrategy(IStrategy):
    def sort(self, items):
        for i in range(0, len(items) - 1):
            min_index = i

            for j in range(i + 1, len(items)):
                if items[j] < items[min_index]:
                    min_index = j

            if min_index != i:
                items[min_index], items[i] = items[i], items[min_index]

        return items