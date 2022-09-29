from strategy import IStrategy


class QuickSortStrategy(IStrategy):
    def sort(self, items):
        if len(items) <= 1:
            return items

        pivot = items.pop()

        greater_than_pivot = []
        less_than_pivot = []

        for item in items:
            if item > pivot:
                greater_than_pivot.append(item)

            else:
                less_than_pivot.append(item)

        return self.sort(less_than_pivot) + [pivot] + self.sort(greater_than_pivot)
