from auth import Auth
from user import User 



auth = Auth()
"""
uid = auth.create_user("test@gmail.com", "testUser")
print("This is the user ID :", uid)

user = User(uid)
postdata = {"audio": "audio.wav",
            "caption": "My audio",
            "likes": [],
            "comments": []}

user.create_post(postdata)
"""
uid = auth.sign_in("test@gmail.com")

user = User(uid)
postdata = {"audio": "audio.wav",
            "caption": "My audio",
            "likes": [],
            "comments": []}

user.getOnePost(2)







