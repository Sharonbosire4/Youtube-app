from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build


SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
CLIENT_SECRETS_FILE = '../client_secrets.json'
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'

# to add the variables to .env

# authenticates user using google oauth2.0 prtocol
def get_authenticated_service():
  flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
  credentials = flow.run_local_server()
  print(credentials.token)
  return build(API_SERVICE_NAME, API_VERSION, credentials = credentials)
