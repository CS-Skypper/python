import os
import re
from datetime import timedelta
from googleapiclient.discovery import build

api_key = os.environ.get('YT_API_KEY')


# youtube service
youtube = build('youtube', 'v3', developerKey=api_key)

hours_pattern = re.compile(r'(\d+)H')
minutes_pattern = re.compile(r'(\d+)M')
seconds_pattern = re.compile(r'(\d+)S')

total_seconds = 0
nextPageToken = None
pl_id_list = []

pl_request = youtube.playlists().list(
  part='contentDetails, snippet',
  channelId="UCCezIgC97PvUuR4_gbFUs5g",
  maxResults=50
)
pl_response = pl_request.execute()
# print(pl_response)


for playlist in pl_response['items']:
  playlist_id = playlist['id']
  pl_id_list.append(playlist_id)

print(len(pl_id_list))


pl_items_request = youtube.playlistItems().list(
  part='contentDetails',
  playlistId=playlist_id,
  maxResults=50,
  pageToken=nextPageToken # for first iteration, "none" will be evaluated as "first"
)
pl_items_response = pl_items_request.execute()



for item in pl_items_response['items']:
  vid_id = item['contentDetails']['videoId']

vid_ids = []
for item in pl_items_response['items']:
  vid_ids.append(item['contentDetails']['videoId'])
# using string join method, that will take every item from the list and separete them with a ','
# print for debug and understanding
# print("video IDs:", ','.join(vid_ids),"\n")

# querry the video resource using the youtube serice (row 8)
# the service takes a "part" argument
vid_request = youtube.videos().list(
  part="contentDetails",
  id=','.join(vid_ids)
)


# print(playlist_id)
# print(pl_items_response)




youtube.close()