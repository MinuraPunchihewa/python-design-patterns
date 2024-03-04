from subject import Subject


class NewsPublisher(Subject):
    def __init__(self) -> None:
        super().__init__()
        self._latest_news = None

    def register(self, observer) -> None:
        self._observers.append(observer)

    def unregister(self, observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self._latest_news)

    @property
    def latest_news(self) -> str:
        return self._latest_news
    
    @latest_news.setter
    def latest_news(self, value: str) -> None:
        self._latest_news = value
        self.notify()