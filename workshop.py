from instagrapi import Client
from instagrapi.types import StoryMention, StoryMedia, StoryLink, StoryHashtag
from exhandler import *

settings = {
    "user_agent": "Instagram 219.0.0.12.117 Android (26/8.0.0; 480dpi; 1080x1920; Xiaomi; MI 5s; capricorn; qcom; en_US; 301484483)"
}
client = Client(settings)
exception_handler(self=None)

class StartupRoutine:
    def __init__(self, welcome, username, password, media_pk, media_path, hashtag):
        self.welcome = welcome
        self.username = username
        self.password = password
        self.media_pk = media_pk
        self.media_path = media_path
        self.hashtag = hashtag       

link = 'https://www.instagram.com/p/ClRT9CkAHRe/'

startUp = StartupRoutine(print("Video to story uploader"),
            input("Username: "), input("Password: "), client.media_pk_from_url(link), 
            client.video_download(client.media_pk_from_url(link)), client.hashtag_info('ucll'))

startUp.welcome
print('Starting bot')
print('Attempting login')
boolLoggedin = client.login(startUp.username, startUp.password, True)

if(boolLoggedin):   
    print("Successfully logged in")
    
    userToMention = client.user_info_by_username('3ict1test1')
    client.video_upload_to_story(
        startUp.media_path,
        mentions=[StoryMention(user=userToMention)],
        links=[StoryLink(webUri='https://github.com/adw0rd/instagrapi')],
        hashtags=[StoryHashtag(hashtag=startUp.hashtag)],
        medias=[StoryMedia(media_pk=startUp.media_pk)])
    
    print("Successfully posted the video!")
        
else:
    print("Could not log in. Check your credentials!")