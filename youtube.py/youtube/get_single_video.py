import json
import sys


from authentication import get_authenticated_service


def get_single_video(video_id):
    youtube = get_authenticated_service()
    results = youtube.videos().list(
    part='snippet,contentDetails,statistics',
    id=video_id).execute()
    # print(json.dumps(results))
    # print(results['items'][0]['contentDetails'])
    items = results['items'][0]
    contentDetails = items['contentDetails']
    statistics = items['statistics']
    duration = contentDetails['duration']
    video_details = {
        'duration': duration,
        'views': statistics['viewCount'],
        'comments': statistics['commentCount'],
        'likes': statistics['likeCount'],
    }
    return video_details

if __name__ == "__main__":
    video_details = get_single_video(sys.argv[1])
    print(video_details)
