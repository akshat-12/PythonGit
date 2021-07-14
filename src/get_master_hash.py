import os
from src.file_utilities import read_file

def get_local_master_hash():
    master_path = os.path.join('.pygit', 'refs', 'heads', 'master')
    try:
        return read_file(master_path).decode().strip()
    except FileNotFoundError:
        return None