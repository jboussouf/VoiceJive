from User import User, getAll_posts, get_all_friends, not_friends, all_msgs
from auth import Auth
from flask import Flask, render_template, request, redirect, session, url_for
from post import Post
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.secret_key = 'secured_session'
auth = Auth()


@app.route('/', methods=['GET', 'POST'])
@cross_origin()
def main():
    if request.method == 'POST' and request.form.get('email', None) != None:
        session['email'] = request.form.get('email', None)
        session['UID'] = auth.sign_in(session['email'])
        return redirect(url_for('index'))
    return render_template('login.html')

#login to an account
@app.route('/login')
def login():
    return render_template('login.html')

#create account
@app.route('/signup')
@cross_origin()
def signin():
    return render_template('signup.html')
#index of our applications (all posts and ability to create post or add new frends)
@app.route('/index')
@cross_origin()
def index():
    if session.get('UID', None) != None:
        all_posts = getAll_posts()
        print(all_posts)
        return render_template('index.html', data = all_posts)
    return render_template('login.html')

#save the audio uploaded by a user
@app.route('/save-audio', methods=['POST'])
@cross_origin()
def save_audio():
    if 'audio' in request.files:
        audio_file = request.files['audio']
        audio_file.save('./recording.wav')
        caption = request.form['caption']
    user = User(session['UID'])
    user.create_post({'audio': './recording.wav', 'caption':caption})
    return redirect('/index')

#redirect to a page for creating a new post
@app.route('/newPost', methods=['POST'])
@cross_origin()
def newPost():
    return render_template('newPost.html')


#get the list of all friends
@app.route('/friends', methods=['POST', "GET"])
@cross_origin()
def friend():
    if session.get('UID', None) != None:
        friends = get_all_friends(session.get('UID', None)) 
        not_friend = not_friends(session.get('UID', None))
        return render_template('friend.html', friends = friends, not_friend = not_friend)
    else:
        return render_template('login.html')
    

#add_friend to list of friends
@app.route('/add_friend', methods=['POST'])
@cross_origin()
def add_friend():
    if request.method == 'POST' and request.form.get('user', None) != None and session.get('UID', None) != None:
        uid = request.form.get('user', None)
        user = User(session.get('UID', None))
        user.add_friend(uid)
        return redirect(url_for("index"))
    else:
        return redirect(url_for('index'))

#create an account in the application
@app.route('/create_account', methods=['POST'])
def create_account():
    if request.method == 'POST' and request.form.get('username', None) != None and request.form.get('email', None) != None and session.get('UID', None) != None:
        username = request.form.get('username', None)
        email = request.form.get('email', None)
        auth.create_user(email, username)
        return redirect(url_for('login'))
    return redirect(url_for('signup'))

#list of messages between friend
@app.route('/communication', methods=["POST", "GET"])
def communication():
    if request.method == 'POST' and request.form.get('uidFriend', None) != None and session.get('UID', None) != None:
        all_mess = all_msgs(session.get('UID'), request.form.get('uidFriend', None))
        print(all_mess)
        session['UIDFriend'] = request.form.get('uidFriend', None)
        return render_template('messages.html', all_mess=all_mess)
    elif session.get('UIDFriend', None) != None and session.get('UID', None) != None:
        all_mess = all_msgs(session.get('UID'), session.get('UIDFriend', None))
        print(all_mess)
        return render_template('messages.html', all_mess=all_mess)
    
#send msg to the friend
@app.route('/send_mgs', methods=["POST"])
def send_msg():
    if request.method == 'POST' and request.form.get('message', None) and session.get('UID', None) != None and session.get('UIDFriend', None) != None:
        user = User(session['UID'])
        user.send_msg(session.get('UIDFriend', None), request.form.get('message', None))
        return redirect(url_for('communication'))
    return redirect(url_for('index'))
    

if __name__ == '__main__':
    app.run(debug=True)
