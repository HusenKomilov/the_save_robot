import requests
import json
from pprint import pprint as pp


def instagram_download(link):
    url = "https://instagram-downloader-download-instagram-videos-stories.p.rapidapi.com/index"

    querystring = {"url": link}

    headers = {
        "X-RapidAPI-Key": "a9f3999afbmshc1ec4950052241bp1e9af3jsn2f117e925fc3",
        "X-RapidAPI-Host": "instagram-downloader-download-instagram-videos-stories.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    res = json.loads(response.text)
    if 'error' in res:
        return 'Bad'
    else:
        date = {}
        if res['Type'] == 'Post-Image':
            date['type'] = 'image'
            date['media'] = res['media']
            return date
        elif res['Type'] == 'Post-Video':
            date['type'] = 'video'
            date['media'] = res['media']
            return date
        elif res['Type'] == 'Carousel':
            date['type'] = 'carousel'
            date['media'] = res['media']
            return date
        elif res['type'] == 'carousel':
            date['type'] = "car"
            date['media'] = res['media']
        else:
            return 'Bad'