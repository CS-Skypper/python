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
while True: # extremely dangerous, provide exit condition
  ch_request = youtube.channels().list(
    part='contentDetails, statistics',
    forUsername='schafer5'
    # forUsername='sentdex'
  )

  pl_request = youtube.playlists().list(
    part='contentDetails, snippet',
    channelId="UCCezIgC97PvUuR4_gbFUs5g",
    maxResults=50
  )
  pl_items_request = youtube.playlistItems().list(
    part='contentDetails',
    playlistId="PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS",
    maxResults=50,
    pageToken=nextPageToken # for first iteration, "none" will be evaluated as "first"
  )

  ch_response = ch_request.execute()
  pl_response = pl_request.execute()
  pl_items_response = pl_items_request.execute()

  for playlist in pl_response['items']:
    playlist_id = playlist['id']
    print(playlist_id)

  # print(pl_response)
  print(pl_items_response)

  for item in pl_items_response['items']:
    vid_id = item['contentDetails']['videoId']
  # print for debug and understanding
    # print("video ID:", vid_id, "\n")

  # need csv string from the list with the vid ids 
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

  vid_response = vid_request.execute()

  for item in vid_response['items']:
    duration = item['contentDetails']['duration']

    raw_hours = hours_pattern.search(duration)
    raw_minutes = minutes_pattern.search(duration)
    raw_seconds = seconds_pattern.search(duration)
    
    # ternary conditional
    ## "I want this value here if raw_hours is not none, if it is none else 0"
    hours = int(raw_hours.group(1)) if raw_hours else 0 # it will fail if the video has no "raw_hour" pattern
    minutes = int(raw_minutes.group(1)) if raw_minutes else 0
    seconds = int(raw_seconds.group(1)) if raw_seconds else 0

    video_seconds = timedelta(
      hours = hours,
      minutes = minutes,
      seconds = seconds
    ).total_seconds()

  # prints for debug and understanding
    # print("\nvideo properties:\n",item,"\n")
    # print(duration,"->",raw_hours,raw_minutes,raw_seconds,"\n")
    # print(type(raw_minutes.group(1)),":",raw_minutes.group(1))
    # print(type(minutes), ":", minutes, "minutes","\n")
    # print("duration:",hours, minutes, seconds)
    # print(int(video_seconds),"seconds")

    total_seconds += video_seconds

  # brake out of the loop once there are no more pages to query
  nextPageToken = pl_items_response.get('nextPageToken')

  if not nextPageToken:
    break


pl_duration = timedelta(seconds=total_seconds)

print(pl_duration)
# print(int(total_seconds))

youtube.close()
