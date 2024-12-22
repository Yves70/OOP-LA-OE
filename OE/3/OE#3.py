class SocialMediaAccount:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        return f"{self.username} has logged in."

    def post(self, content):
        return f"{self.username} posted: {content}"

class InstagramAccount(SocialMediaAccount):
    def __init__(self, username, password, number_of_followers):
        super().__init__(username, password)
        self.number_of_followers = number_of_followers

    def share_story(self):
        return f"{self.username} shared a story with {self.number_of_followers} followers."

class TwitterAccount(SocialMediaAccount):
    def __init__(self, username, password, number_of_tweets):
        super().__init__(username, password)
        self.number_of_tweets = number_of_tweets

    def tweet(self, tweet_content):
        self.number_of_tweets += 1
        return f"{self.username} tweeted: {tweet_content}. Total tweets: {self.number_of_tweets}"

insta_user = InstagramAccount("insta_user", "password123", 500)
print(insta_user.login()) 
print(insta_user.post("Check out my new photo!")) 
print(insta_user.share_story()) 

twitter_user = TwitterAccount("twitter_user", "password123", 100)
print(twitter_user.login())
print(twitter_user.post("Hello world!"))
print(twitter_user.tweet("Just tweeted this!")) 
