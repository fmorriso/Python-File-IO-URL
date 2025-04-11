import sys

import requests
from requests import Response


def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'


def convert_google_drive_public_link_to_readable_url(link: str) -> str:
    """
    Converts a Google Drive share link for a file to one that can be used to read the file contents:
    :param link: the original link
    :return: a URL string that can be used to read the file contents

    Example input:
    https://drive.google.com/file/d/1cU2M7HNdKLl8GXpXujgRwxBMGhlfmwHm/view?usp=sharing
    """
    find_start_of_id = 'file/d/'
    start_index = link.index(find_start_of_id) + len(find_start_of_id)
    ending_index = link.index('/view?')
    id = link[start_index:ending_index]
    # print(f'{id = }')
    return f'https://drive.google.com/uc?export=download&id={id}'


print(f'File I/O from URL using python version {get_python_version()}')

# My Drive > public > python code snippets.txt
google_share_link = 'https://drive.google.com/file/d/1cU2M7HNdKLl8GXpXujgRwxBMGhlfmwHm/view?usp=sharing'
readable_url = convert_google_drive_public_link_to_readable_url(google_share_link)

resp: Response = requests.get(readable_url)
binary_string_content: bytes = resp.content  # binary string

# now convert binary string to regular string
string_content = binary_string_content.decode('utf-8')

# echo each line from the text file
for line in string_content.splitlines():
    print(line)
