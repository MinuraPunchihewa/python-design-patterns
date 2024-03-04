from observer import Observer


class NewsSubscriber(Observer):
    def __init__(self, name: str):
        self.name = name

    def update(self, message: str) -> None:
        print(f"{self.name} received: {message}")