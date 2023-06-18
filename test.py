from auth import Auth
from user import User 



auth = Auth()
"""
data = {
    'name': 'John Doe',
    'age': 30,
    'email': 'johndoe@example.com',
    'informations':{
        'job':['AI', 'ML', 'LLM'],
        'socity':'IBM',
        'experience':15
    }
}
user.add_data("users.name",data)"""

uid = auth.sign_in("issam@issam.com")
print(uid)

user = User(uid)
user.create_post("hello! it's my first post")



