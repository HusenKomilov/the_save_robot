import requests
import json


def tiktok_save(link):
    url = "https://tiktok-video-no-watermark2.p.rapidapi.com/"

    querystring = {"url": link, "hd": "0"}

    headers = {
        "X-RapidAPI-Key": "a9f3999afbmshc1ec4950052241bp1e9af3jsn2f117e925fc3",
        "X-RapidAPI-Host": "tiktok-video-no-watermark2.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    res = json.loads(response.text)
    main = res['data']['play']
    return {'video': main}

