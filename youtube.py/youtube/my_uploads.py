#!/usr/bin/python


import argparse
import os
import re

from authentication import get_authenticated_service


SCOPES = ['https://www.googleapis.com/auth/youtube.readonly']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'

def get_my_uploads_list():
  youtube = get_authenticated_service()
  channels_response = youtube.channels().list(
    mine=True,
    part='contentDetails'
  ).execute()

  playlists_uploads_id = []


  for channel in channels_response['items']:

    playlist_upload_id = channel['contentDetails']['relatedPlaylists']['uploads']
    print(playlist_upload_id)
    playlists_uploads_id.append(playlist_upload_id)

  return playlists_uploads_id

if __name__ == "__main__":
    ids = get_my_uploads_list()
    print(ids)