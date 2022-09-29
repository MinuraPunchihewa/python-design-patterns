from strategy import IStrategy


class BubbleSortStrategy(IStrategy):
    def sort(self, inputs):
        sorted = False

        while not sorted:
            sorted = True
            for i in range(0, len(inputs) - 1):
                if inputs[i + 1] < inputs[i]:
                    sorted = False
                    inputs[i], inputs[i + 1] = inputs[i + 1], inputs[i]

        return inputs
    