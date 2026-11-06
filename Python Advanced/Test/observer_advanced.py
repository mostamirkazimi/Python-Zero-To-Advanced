class User:

    def update(
        self,
        message
    ):
        print(message)


class Blog:

    def __init__(self):

        self.users = []

    def subscribe(
        self,
        user
    ):
        self.users.append(
            user
        )

    def notify(
        self,
        message
    ):

        for user in self.users:

            user.update(
                message
            )


blog = Blog()

user = User()

blog.subscribe(user)

blog.notify(
    "New Post Published"
)