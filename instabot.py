from flask import Flask, render_template, request
from instagrapi import Client
from exhandler import *

client = Client()
app = Flask(__name__)

@app.route('/')
def index():
    
    return render_template('index.html')

@app.route('/instabot', methods=['POST','GET'])
def instabot():
    
    exception_handler(self=None)
    list = []
    
    print("Starting bot")
    print("Attempting login")
   
    boolLoggedin = client.login(request.form['username'], request.form['password'], True)
    print("Successfully logged in")

    if (boolLoggedin):
        print(f"Getting posts from hashtag {request.form['hashtag']}")
        posts = client.hashtag_medias_recent(request.form['hashtag'], int(request.form['amount']))

        if (len(posts) > 0) :
            for index in range(len(posts)):
                media = posts[index]

                client.media_like(media.id)
                print(f"Liked post {index+1} with #{request.form['hashtag']} by @{media.user.username}")
                    
                # if (index % 5 == 0):         
                client.user_follow(media.user.pk)
                print(f"Followed @{media.user.username}")
                
                client.media_comment(media.id,request.form['caption'])
                print(f"Commented with: {request.form['caption']} on post {index+1}") 
                
                list.append(media.thumbnail_url)          
                print(list)
        else:
            print("Could not find any posts regarding the hashtag")
    else:
        print("Could not log in, check credentials") 
         
    return render_template('image.html', len=len(list), list=list)

if (__name__ == "__main__"):
    app.run(debug=True)