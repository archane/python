#!/usr/bin/env python
# Created by Frank Jensen
# This code printed out the username and msg of anyone in the follow list to stdout
# Tweepy is the only required module for this program

from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from tweepy import Stream
import json
from StringIO import StringIO
consumer_key=''
consumer_secret=''
access_token=''
access_token_secret=''
follow_list = ['25073877','1339835893','13115682','822215679726100480','822215673812119553'] #these are just examples
#follow list = trump,hilary,azcentral,POTUS,whitehouse

class StdOutListener(StreamListener):

    def on_status(self, status):
        user_json = json.load(StringIO(json.dumps(status._json['user'])))
        user_lang = json.dumps(user_json['lang'])
        user_id = json.dumps(user_json['id'])
        is_reply = status.in_reply_to_status_id
        temp_user = json.dumps(user_json['screen_name'])
        if user_lang == '"en"': # and user_id in follow_list:
                print(temp_user.ljust(20) + "," + status.text)
    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False
        print(status_code)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(follow=follow_list)

