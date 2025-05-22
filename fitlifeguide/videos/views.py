# from django.shortcuts import render
# from django.conf import settings
# import requests

# def videos_views(request):
#     url = 'https://www.googleapis.com/youtube/v3/search'
#     video_url = 'https://www.googleapis.com/youtube/v3/videos'


#     search_params = {
#         'part' : 'snippet',
#         'q' : 'workout videos',
#         'key' : settings.YOUTUBE_DATA_API_KEY,
#         'type' : 'video',
#         'maxResults' : 15
#     }

#     video_ids = []
#     r = requests.get(url, params=search_params)

#     results = r.json()['items']

#     for result in results:
#         video_ids.append(result['id']['videoId'])

#     video_params = {
#         'part' : 'snippet,contentDetails',
#         'key' : settings.YOUTUBE_DATA_API_KEY,
#         'id' : ','.join(video_ids)
#     }
    
#     r = requests.get(video_url, params=video_params)
    
#     results = r.json()['items']

#     for result in results:
#         # print(result['title'])
#         print(result['id'])
#         print(result['contentDetails']['duration'])
#         print(result['thumbnails']['high']['url'])



#     return render(request, 'videos/videos.html')




from django.shortcuts import render
from django.conf import settings
import requests
import isodate  # <--- import this
import datetime

def format_duration(iso_duration):
    try:
        duration = isodate.parse_duration(iso_duration)
        total_seconds = int(duration.total_seconds())
        return str(datetime.timedelta(seconds=total_seconds))
    except Exception:
        return "N/A"

def videos_views(request):
    search_url = 'https://www.googleapis.com/youtube/v3/search'
    video_url = 'https://www.googleapis.com/youtube/v3/videos'

    search_params = {
        'part': 'snippet',
        'q': 'workout',
        'key': settings.YOUTUBE_DATA_API_KEY,
        'type': 'video',
        'maxResults': 15
    }

    search_response = requests.get(search_url, params=search_params)
    search_results = search_response.json().get('items', [])
    video_ids = [result['id']['videoId'] for result in search_results]

    video_params = {
        'part': 'snippet,contentDetails',
        'key': settings.YOUTUBE_DATA_API_KEY,
        'id': ','.join(video_ids)
    }

    video_response = requests.get(video_url, params=video_params)
    video_results = video_response.json().get('items', [])

    videos = []

    for result in video_results:
        snippet = result.get('snippet', {})
        content_details = result.get('contentDetails', {})

        iso_duration = content_details.get('duration')
        readable_duration = format_duration(iso_duration)

        video = {
            'id': result.get('id'),
            'title': snippet.get('title'),
            'thumbnail': snippet.get('thumbnails', {}).get('high', {}).get('url'),
            'duration': readable_duration,
        }
        videos.append(video)


    return render(request, 'videos/videos.html', {'videos': videos})
