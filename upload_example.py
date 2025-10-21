import requests
import json
import os

payload = {
    'cover_time': '0.0',
    'description': 'test #test',
    'hashtags': ['#test'],
    'music_id': '6817665487665629186',
    'is_comments_enabled': True,
    'is_auto_caption_enabled': True,
    'is_audience_control_enabled': False,
    'is_duet_enabled': True,
    'is_stitch_enabled': True,
    'is_ai_generated_content_enabled': False,
    'is_gallery_upload': True
}

files = [
    ('data', (None, json.dumps(payload), 'application/json')),
]


#fщк upload 1 photo
#files.append(('images[]', (os.path.basename(r"patch"), open(r"patch", 'rb'), 'application/octet-stream')))

#for upload 2 photo
#files.append(('images[]', (os.path.basename(r"patch"), open(r"patch", 'rb'), 'application/octet-stream')))
#files.append(('images[]', (os.path.basename(r"patch"), open(r"patch", 'rb'), 'application/octet-stream')))

#for video upload
#files.append(('video', (os.path.basename(r"patch"), open(r"patch", 'rb'), 'video/mp4')))

new_headers = {
    'x-device': "REPLACE",
    'x-cookie': "REPLACE",
    'x-proxy': "REPLACE",
} 


default_headers = {
    'X-Api-Key': "REPLACE",
}
new_headers.update(default_headers)
responce = requests.post(f'https://tikown.app/api/post/create',params={'region':"DE"}, files=files, headers=new_headers)


jso121212 = responce.json()

print(f"Status Code: {responce.status_code}")
print("Response:")
print(json.dumps(responce.json(), indent=2))