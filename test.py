from auth import Auth
from User import User 
import datetime

current_date = datetime.date.today()
formatted_date = current_date.strftime("%B %d, %Y")




auth = Auth()
"""
uid1 = auth.create_user("test1@gmail.com", "test1")
uid2 = auth.create_user("test2@gmail.com", "test2")
uid3 = auth.create_user("test3@gmail.com", "test3")
#print("This is the user ID :", uid2)"""

uid1 = auth.sign_in("test1@gmail.com")
#print(uid2)
#
user1 = User(uid1)

#user.send_msg(uid2, "I'm great, so tell me about the fact that zdagadag")
postdata = {"audio": "recording.wav",
            "caption": "My second audio",
            "date": formatted_date}

user1.create_post(postdata)
'''
postdata = {"audio": "audio.wav",
            "caption": "My audio",
            "likes": [],
            "comments": []}
'''





