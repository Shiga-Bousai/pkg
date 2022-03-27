import requests
import os
import json
import time

from .twitterOAuth1 import oath
oauth = oath()

def INITMedia(filePath,fileType):
    fileTypeDict = {
        'video' : ['tweet_video','video/mp4'],
        'gif' : ['tweet_gif','image/gif'],
        'png' : ['tweet_image','image/png'],
        'jpeg' : ['tweet_image','image/jpeg']
    }

    file_size = os.path.getsize(filePath) 
    print(file_size)
    apiEndPoint = f'https://upload.twitter.com/1.1/media/upload.json'
    req_body = {
        'command':'INIT',
        'total_bytes' : file_size,
        'media_type': fileTypeDict[fileType][1],
        'media_category' : fileTypeDict[fileType][0]
    }
    response = requests.post(
        apiEndPoint,
        files=req_body,
        auth=oauth
    )
    resJson = json.loads(response.text)
    print("INIT :", response.status_code, response.text)
    return resJson["media_id_string"]

def APPENDMedia(filePath, mediaID):
    apiEndPoint = f'https://upload.twitter.com/1.1/media/upload.json'
    file_size = os.path.getsize(filePath) 
    uploadFile = open(filePath, 'rb')
    index = 0
    while True:
        data = uploadFile.read(4 * 1024 * 1024)
        if len(data) == 0:
            break
        req_body = {
            'command':'APPEND',
            'media_id':mediaID,
            'segment_index':index
        }
        req_files = {'media':data}
        response = requests.post(
            apiEndPoint,
            data=req_body,
            files=req_files,
            auth=oauth
        )
        print("APPEND :",response.status_code, response.text)
        index += 1
    uploadFile.close()

def STATUSMedia(mediaID):
    apiEndPoint = f'https://upload.twitter.com/1.1/media/upload.json'
    request_params = {'command': 'STATUS','media_id': mediaID}
    processPercent = 0
    while(processPercent < 100):
        response = requests.get(
            apiEndPoint,
            params=request_params,
            auth=oauth
        )
        res = json.loads(response.text)
        processPercent = res['processing_info']['progress_percent']
        print("STATUS :",res, processPercent)
        time.sleep(1)

def FINALIZEMedia(mediaID):
    apiEndPoint = f'https://upload.twitter.com/1.1/media/upload.json'
    request_data = {
        'command': 'FINALIZE',
        'media_id': mediaID
    }

    req = requests.post(url=apiEndPoint, data=request_data, auth=oauth)
    print("FINALIZE :",req.status_code,req.text)

def lageMediaUpload(filePath,fileType):
    mediaID = INITMedia(filePath,fileType)
    APPENDMedia(filePath, mediaID)
    FINALIZEMedia(mediaID)
    STATUSMedia(mediaID)

    return mediaID

def uploadImage(filePath):
    apiEndPoint = f'https://upload.twitter.com/1.1/media/upload.json'
    uploadFile = open(filePath, 'rb')
    data = uploadFile.read()
    req_files = {'media':data}
    response = requests.post(
        apiEndPoint,
        files=req_files,
        auth=oauth
    )
    uploadFile.close()
    res = json.loads(response.text)
    print(response.status_code, response.text,res['media_id_string'])
    mediaID = res['media_id_string']
    print(mediaID)

    return mediaID