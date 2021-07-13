from getmasterhash import get_local_master_hash
from object_utilities import read_object

def log():
    head_sha = get_local_master_hash()
    get_log(head_sha)

def get_log(commit_hash):
    type, data = read_object(commit_hash)
    data = data.decode()
    print(data)
    x = data.find('parent')
    if x == -1:
        return
    else:
        parent_sha = data[x+7:x+47]
        get_log(parent_sha)