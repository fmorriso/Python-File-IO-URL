import sys


def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'


print(f'File I/O from URL using python version {get_python_version()}')