import io
import sys

import requests
import urllib3
import pandas as pd

def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'

def convert_google_drive_public_link_to_url(link: str) -> str:
    starting_token = 'file/d/'

    return f'https://drive.google.com/uc?export=download&id={link}'

# My Drive > public > gitlab-example.txt
# https://drive.google.com/file/d/1cU2M7HNdKLl8GXpXujgRwxBMGhlfmwHm/view?usp=drive_link
# https://drive.google.com/file/d/1cU2M7HNdKLl8GXpXujgRwxBMGhlfmwHm/view?usp=drive_link


# https://drive.google.com/file/d/13v8F280YBjJHnJlOBQsEtd0dtG8nJXXc/view
# https://drive.google.com/file/d/13v8F280YBjJHnJlOBQsEtd0dtG8nJXXc/view?usp=sharing
# https://drive.google.com/file/d/13v8F280YBjJHnJlOBQsEtd0dtG8nJXXc/view?usp=drive_link
# https://drive.google.com/cu?export=download&id
print(f'File I/O from URL using python version {get_python_version()}')
# id = '13v8F280YBjJHnJlOBQsEtd0dtG8nJXXc'
id = '1cU2M7HNdKLl8GXpXujgRwxBMGhlfmwHm' # python code snippets.txt
# https://drive.google.com/file/d/1cU2M7HNdKLl8GXpXujgRwxBMGhlfmwHm/view?usp=sharing
url = f'https://drive.google.com/uc?export=download&id={id}'
print(f'url: {url}')
# resp = urllib3.request('GET', url, decode_content = True)
# print(f'{resp.status = }')
# print(f'{resp.data = }')

# import urllib.request
# for line in urllib.request.urlopen(url):
#     print(line.decode('utf-8'))

#FAILS with JSONDecodeError: print(resp.json())
# for line in resp.data.splitlines():
#     print(line)
# df = pd.read_csv(url, sep='', header = None)
# print(f'type(df): {type(df)}')

s = requests.get(url)
print(f'status_code: {s.status_code}')
b_content = s.content
print(f'{b_content = }')
s_content = b_content.decode('utf-8')
# print(f'{s_content = }')
for line in s_content.splitlines():
    print(line)
