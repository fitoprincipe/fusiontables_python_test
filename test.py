import os
import pprint

# import google.oauth2.credentials

from googleapiclient.discovery import build
# from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow

pp = pprint.PrettyPrinter(indent=2)

# The CLIENT_SECRETS_FILE variable specifies the name of a file that contains
# the OAuth 2.0 information for this application, including its client_id and
# client_secret.
CLIENT_SECRETS_FILE = "client_secret.json"

# This access scope grants read-only access to the authenticated user's Drive
# account.
SCOPES = ['https://www.googleapis.com/auth/fusiontables']
API_SERVICE_NAME = 'fusiontables'
API_VERSION = 'v2'
TABLE_ID = '1RnoPAPBChUZHfSarqFUszGHI8CHseyUPY1UaqcYT'

def get_authenticated_service():
  flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
  credentials = flow.run_console()
  return build(API_SERVICE_NAME, API_VERSION, credentials = credentials)

def get_table(service):
  results = service.table().get(tableId=TABLE_ID)
  request = results.execute()
  pp.pprint(request)

if __name__ == '__main__':
  # When running locally, disable OAuthlib's HTTPs verification. When
  # running in production *do not* leave this option enabled.
  os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
  service = get_authenticated_service()
  get_table(service)