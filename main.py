import sys
import urllib3

def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'

def convert_google_drive_public_link_to_url(link: str) -> str:
    starting_token = 'file/d/'

    return f'https://drive.google.com/uc?export=download&id={link}'


# https://drive.google.com/file/d/13v8F280YBjJHnJlOBQsEtd0dtG8nJXXc/view
# https://drive.google.com/file/d/13v8F280YBjJHnJlOBQsEtd0dtG8nJXXc/view?usp=sharing
# https://drive.google.com/file/d/13v8F280YBjJHnJlOBQsEtd0dtG8nJXXc/view?usp=drive_link
# https://drive.google.com/cu?export=download&id
print(f'File I/O from URL using python version {get_python_version()}')
id = '13v8F280YBjJHnJlOBQsEtd0dtG8nJXXc'
url = f'https://drive.google.com/uc?export=download&id={id}'
# resp = urllib3.request('GET', url, decode_content = True)
# print(f'{resp.status = }')
# print(f'{resp.data = }')

import urllib.request
for line in urllib.request.urlopen(url):
    print(line.decode('utf-8'))
#FAILS with JSONDecodeError: print(resp.json())
# for line in resp.data.splitlines():
#     print(line)
