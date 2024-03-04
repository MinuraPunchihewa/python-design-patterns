from news_publisher import NewsPublisher
from news_subscriber import NewsSubscriber


news_publisher = NewsPublisher()

john = NewsSubscriber("John")
lisa = NewsSubscriber("Lisa")

news_publisher.register(john)
news_publisher.register(lisa)

news_publisher.latest_news = "Hello, World!"

news_publisher.unregister(john)

news_publisher.latest_news = "Hello, World! Again!"