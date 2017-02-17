#!/usr/bin/env python
# Created by Frank Jensen
# This feed printed out every tweet in a square covering most of Arizona
#Tweepy is the only required module for this program

from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from tweepy import Stream
import json
from StringIO import StringIO
consumer_key=''
consumer_secret=''
access_token=''
access_token_secret=''

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
            return False
        print(status_code)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(locations=[-114.7739,32.50547,-109.096955,36.972059])
