import urllib.request
import json
from settings import API_KEY

CHANNEL_ID = 'UC7o64rkXin-ZS_gU6_pBDvA'
api_key = API_KEY
print(api_key)

def get_all_video_in_channel(channel_id):
    

    base_video_url = 'https://www.youtube.com/watch?v='
    base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

    first_url = base_search_url+'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(api_key, channel_id)

    video_links = []
    url = first_url
    while True:
        inp = urllib.request.urlopen(url)
        resp = json.load(inp)

        for i in resp['items']:
            if i['id']['kind'] == "youtube#video":
                video_links.append(base_video_url + i['id']['videoId'])

        try:
            next_page_token = resp['nextPageToken']
            url = first_url + '&pageToken={}'.format(next_page_token)
        except:
            break
    return video_links


# video_url_list = get_all_video_in_channel(CHANNEL_ID)
# print(len(video_url_list))
