import datetime
from datetime import datetime
from Google import Create_Service
from googleapiclient.http import MediaFileUpload


print("Required Libraries are imported .........")



CLIENT_SECRET_FILE = '/Users/neerajsingh/Documents/projects/youtube_automation/client_secret.json'
API_NAME = 'youtube'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/youtube.upload']


service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

now  = datetime.now()
print(now)
upload_date_time = datetime(2022, 8, 24, 9, 45, 0).isoformat() + '.000Z'

request_body = {
    'snippet': {
        'categoryI': 19,
        'title': 'Upload Testing',
        'description': 'Hello World Description',
        'tags': ['Travel', 'video test', 'Travel Tips']
    },
    'status': {
        'privacyStatus': 'private',
        'selfDeclaredMadeForKids': False, 
    },
    'notifySubscribers': False
}

mediaFile = MediaFileUpload('/Users/neerajsingh/Documents/projects/youtube_automation/testing.mov')

response_upload = service.videos().insert(
    part='snippet,status',
    body=request_body,
    media_body=mediaFile
).execute()



service.thumbnails().set(
    videoId=response_upload.get('id'),
    media_body=MediaFileUpload('/Users/neerajsingh/Documents/projects/youtube_automation/10x-featured-social-media-image-size.png')
).execute()
