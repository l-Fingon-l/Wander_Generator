import requests
from PIL import Image
from io import BytesIO


def get_thumbnails(channel_id, img_path):
    api_key = input('API key: ')
    base_video_url = 'https://img.youtube.com/vi/'
    base_video_end = '/mqdefault.jpg'
    base_search_url = 'https://www.googleapis.com/youtube/v3/search?'
    first_url = base_search_url+'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(api_key, channel_id)

    url = first_url
    name_id = 501
    while True:
        resp = requests.get(url).json()

        for i in resp['items']:
            if i['id']['kind'] == "youtube#video":
                img_url = base_video_url + i['id']['videoId'] + base_video_end
                img_data = requests.get(img_url).content
                img = Image.open(BytesIO(img_data))
                img = img.resize((img.size[1], img.size[1]), Image.ANTIALIAS)
                img.save(img_path + str(name_id) + '.jpg')
                name_id += 1

        next_page_token = resp['nextPageToken']
        url = first_url + '&pageToken={}'.format(next_page_token)


Wanderbraun_id = 'UCOBFz0mX8lL5GSXfDkqu9_g'
WanderbraunGaming_id = 'UCLqdi5MHui0yr8D6LFDWBBA'

get_thumbnails(Wanderbraun_id, 'images/wc3/')
get_thumbnails(WanderbraunGaming_id, 'images/aoe/')

