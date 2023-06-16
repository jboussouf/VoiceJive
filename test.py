from firebase import Firebase

user = Firebase()
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
user.add_data("users.name",data)