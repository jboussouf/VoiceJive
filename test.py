from auth import Auth
from user import User 



auth = Auth()

#uid2 = auth.create_user("test3@gmail.com", "test2User")
#print("This is the user ID :", uid2)

uid2 = auth.sign_in("test3@gmail.com")

uid = auth.sign_in("test@gmail.com")

user = User(uid)
user2 = User(uid2)

user.send_msg(uid2, "I'm great, so tell me about the fact that zdagadag")



'''
postdata = {"audio": "audio.wav",
            "caption": "My audio",
            "likes": [],
            "comments": []}
'''





