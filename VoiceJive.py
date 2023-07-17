from User import User, getAll_posts, get_all_friends, not_friends
from auth import Auth
from flask import Flask, render_template, request, redirect, session, url_for
from post import Post
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.secret_key = 'secured_session'

@app.route('/', methods=['GET', 'POST'])
@cross_origin()
def main():
    if request.method == 'POST' and request.form.get('email', None) != None:
        session['email'] = request.form.get('email', None)
        auth = Auth()
        session['UID'] = auth.sign_in(session['email'])
        print(session['UID'])
        return redirect(url_for('index'))
    return render_template('login.html')

#cc
@app.route('/signup')
@cross_origin()
def signin():
    return render_template('signup.html')

@app.route('/index')
@cross_origin()
def index():
    if session.get('UID', None) != None:
        all_posts = getAll_posts()
        print(all_posts)
        return render_template('index.html', data = all_posts)
    return render_template('login.html')

@app.route('/save-audio', methods=['POST'])
@cross_origin()
def save_audio():
    if 'audio' in request.files:
        audio_file = request.files['audio']
        audio_file.save('./recording.wav')

        caption = request.form['caption']
        print(caption)
    user = User(session['UID'])
    user.create_post({'audio': './recording.wav', 'caption':caption})
    return redirect('/index')


@app.route('/newPost', methods=['POST'])
@cross_origin()
def newPost():
    return render_template('newPost.html')


############ get friends
@app.route('/friends', methods=['post'])
@cross_origin()
def friend():
    if session.get('UID', None) != None:
        friends = get_all_friends(session.get('UID', None)) 
        not_friend = not_friends(session.get('UID', None))
        print(not_friend)
        return render_template('friend.html', friends = friends, not_friend = not_friend)
    else:
        return render_template('login.html')
    


@app.route('/add_friend', methods=['post'])
@cross_origin()
def add_friend():
    if request.method == 'POST' and request.form.get('user', None) != None and session.get('UID', None) != None:
        uid = request.form.get('user', None)
        user = User(session.get('UID', None))
        print(uid)
        user.add_friend(uid)
        return redirect(url_for("/friends"))
    else:
        return redirect(url_for('/index'))

if __name__ == '__main__':
    app.run(debug=True)
