from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import build
import pprint
import os

SCOPE = ['https://www.googleapis.com/auth/fusiontables']
API_SERVICE_NAME = 'fusiontables'
API_VERSION = 'v2'
TABLE_ID = '1RnoPAPBChUZHfSarqFUszGHI8CHseyUPY1UaqcYT'

pp = pprint.PrettyPrinter(indent=2)

def authorize():
    ''' authorize service account using json file 
    
    :return: 
    '''
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
                  'service_key.json', SCOPE)
    return build(API_SERVICE_NAME, API_VERSION, credentials = credentials)

def get_table(service):
  results = service.table().get(tableId=TABLE_ID)
  request = results.execute()
  pp.pprint(request)

if __name__ == '__main__':
  # When running locally, disable OAuthlib's HTTPs verification. When
  # running in production *do not* leave this option enabled.
  os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
  service = authorize()
  get_table(service)