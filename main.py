import sys

import requests
from requests import Response

from program_settings import ProgramSettings


def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'


def get_requests_version() -> str:
    return requests.__version__


def convert_google_drive_public_link_to_readable_url(google_shared_file_link: str) -> str:
    """
    Converts a Google Drive share link for a file to one that can be used to read the file contents:
    :param google_shared_file_link: the original link
    :return: a URL string that can be used to read the file contents

    Example input value:
    https://drive.google.com/file/d/1cU2M7HNdKLl8GXpXujgRwxBMGhlfmwHm/view?usp=sharing

    Example return value:
    'https://drive.google.com/uc?export=download&id=1cU2M7HNdKLl8GXpXujgRwxBMGhlfmwHm'
    """
    find_start_of_id = 'file/d/'
    start_index = google_shared_file_link.index(find_start_of_id) + len(find_start_of_id)
    ending_index = google_shared_file_link.index('/view?')
    file_id_extracted = google_shared_file_link[start_index:ending_index]
    usable_link: str = f'https://drive.google.com/uc?export=download&id={file_id_extracted}'
    return usable_link


### MAIN LOGIC BEGINS HERE ###
print(f'File I/O from URL using python version {get_python_version()} and requests version {get_requests_version()}')

# My Drive > public > python code snippets.txt
google_text_file_shared_link: str = ProgramSettings.get_setting('GOOGLE_SHARED_TEXT_FILE_LINK')
readable_text_file_url = convert_google_drive_public_link_to_readable_url(google_text_file_shared_link)

resp: Response = requests.get(readable_text_file_url)
# the response content is considered a python binary string (e.g., b'some text')
binary_string_content: bytes = resp.content  # binary string, a.k.a class bytes(Sequence[int])

# now convert binary string to regular string
string_content: str = binary_string_content.decode('utf-8')

# echo each line from the text file
for line in string_content.splitlines():
    print(line)
