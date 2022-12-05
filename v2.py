from instagrapi import Client

client = Client()

class StartupRoutine:
    def __init__(self, welcome, insta_username, insta_password, hashtag, caption, amount):
        self.welcome = welcome
        self.insta_username = insta_username
        self.insta_password = insta_password
        self.hashtag = hashtag
        self.caption = caption
        self.amount = int(amount)

startUp = StartupRoutine(print("Instagram Bot by Mustafa & Yasin"), input("Username: "), input("Password: "), input("Hashtag: "), input("Caption: "), input("Amount?: "))
startUp.welcome
print("Starting bot")
print("Attempting login")
boolLoggedin = client.login(startUp.insta_username, startUp.insta_password, True)
print("Successfully logged in")

print(f"Getting posts from hashtag {startUp.hashtag}")
if (boolLoggedin):
    posts = client.hashtag_medias_top(startUp.hashtag, startUp.amount)

    if (len(posts) > 0) :
        for index in range(len(posts)):
            media = posts[index]
            
            #print(media.thumbnail_url)

            # print(f"{media.user.username}, post id {media.id}")
            inf = client.media_like(media.id)
            print(f"Liked post {index+1} with #{startUp.hashtag} by @{media.user.username}")
                
            if (index % 5 == 0):         
                client.user_follow(media.user.pk)
                print(f"Followed @{media.user.username}")
        
                client.media_comment(media.id,startUp.caption)
                print(f"Commented with: {startUp.caption} on post {index+1}")

    else:
        print("Could not find any posts regarding the hashtag")
else:
    print("Could not log in, check credentials")