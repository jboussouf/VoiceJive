
""" structure de post

"""

class Post():

    def __init__(self, audio, caption):
        self.caption = caption
        self.audio = audio
        self.likes = []
        self.comments = []

    def add_like(self, user):
        self.likes.append(user)

    def add_comment(self, user, comment):
        self.comments.append((user, comment))