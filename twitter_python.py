from ast import Num
import requests

import sys
import os
sys.path.append(os.path.abspath("./"))
from pkg.twitterModule import mediaUpload,twitterOAuth1

oauth = twitterOAuth1.oath()

def uploadImage(filePath):
    return mediaUpload.uploadImage(filePath)
def uploadLageMedia(filePath,filetype):
    return mediaUpload.lageMediaUpload(filePath,filetype)

def tweet(content, mediaIDs=None, replyID=None):
    print(content, mediaIDs)
    req_content = {"text": content}
    if (mediaIDs):
        req_content['media'] = {'media_ids' : mediaIDs}
    if (replyID):
        req_content['reply'] = {'in_reply_to_tweet_id' : replyID}
    print(req_content)
    response = requests.post(
        "https://api.twitter.com/2/tweets",
        json=req_content,
        auth=oauth
    )
    if response.status_code != 201:
        raise Exception("Request returned an error: {} {}".format(response.status_code, response.text))
    print("Response code: {}".format(response.status_code))
    json_response = response.json()
    print(json_response)
    return json_response

def tweetThread(contents):
    reply = Num
    returnJson = tweet(contents[0])
    reply = returnJson["data"]["id"]
    contents.pop(0)
    for content in contents:
        returnJson = tweet(content, replyID=reply)
        reply = returnJson["data"]["id"]