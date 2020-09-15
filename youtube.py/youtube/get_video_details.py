import sys

from authentication import get_authenticated_service

def get_video_duration(uploads_playlist_id):
  # Retrieve the list of videos uploaded to the authenticated user's channel.
  youtube = get_authenticated_service()
  playlistitems_list_request = youtube.playlistItems().list(
    playlistId=uploads_playlist_id,
    part='snippet,contentDetails',
    maxResults=5
  )

  print(playlistitems_list_request)
  while playlistitems_list_request:
    playlistitems_list_response = playlistitems_list_request.execute()

    all_video_data = []
    for playlist_item in playlistitems_list_response['items']:
      title = playlist_item['snippet']['title']
      video_id = playlist_item['snippet']['resourceId']['videoId']
      date_published =  playlist_item['snippet']['publishedAt']
      video_data = {
          'id': video_id,
          'name': title,
          'date_time_published': date_published,
      }
      all_video_data.append(video_data)
      playlistitems_list_request = youtube.playlistItems().list_next(
      playlistitems_list_request, playlistitems_list_response)
  return all_video_data

if __name__ == "__main__":
    video = get_video_duration(sys.argv[1])
    print(video)