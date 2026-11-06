class Subscriber:

    def update(self, message):

        print(message)


class Channel:

    def __init__(self):

        self.subscribers = []

    def subscribe(

        self,

        subscriber

    ):

        self.subscribers.append(
            subscriber
        )

    def notify(

        self,

        message

    ):

        for subscriber in self.subscribers:

            subscriber.update(
                message
            )


channel = Channel()

user = Subscriber()

channel.subscribe(user)

channel.notify(
    "New Video Uploaded"
)
