from flask import Flask, render_template, request
from interactivespotify import get_limit


app = Flask(__name__)

default_limit = 10
default_keyword = 'Olly'
# set up our landing page
@app.route('/')
def index():
	my_playlist_id = get_limit(default_limit, default_keyword)
	return render_template('index.html', keyword=default_keyword, limit=default_limit, playlist_id=my_playlist_id)

# only use this when posting data!
@app.route('/', methods=['POST'])
def index_post():
	user_limit = request.form['req_limit']
	user_keyword = request.form['req_keyword']
	my_playlist_id = get_limit(user_limit, user_keyword)
	return render_template('index.html', keyword=user_keyword, limit=user_limit, playlist_id=my_playlist_id)