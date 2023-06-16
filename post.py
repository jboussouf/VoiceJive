


class Post():
    content = {"caption": "", "audio": None}

    def __init__(self, content):
        self.content = content
        self.likes = []
        self.comments = []

    def add_like(self, user):
        self.likes.append(user)

    def add_comment(self, user, comment):
        self.comments.append((user, comment))