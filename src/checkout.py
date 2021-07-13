import os
from getmasterhash import get_local_master_hash
from object_utilities import read_object
from read_tree import read_tree
from file_utilities import write_file

def checkout(commit_message):
    for f in os.listdir(os.getcwd()):
        if not os.path.isdir(f):
            os.remove(os.path.join(os.getcwd(), f))
    master_hash = get_local_master_hash()
    commit_hash = checkout_recur(master_hash, commit_message)
    if commit_hash == -1:
        raise Exception("No commit with said message")
    print(commit_hash)
    obj_type, data = read_object(commit_hash)
    tree_sha = data[5:45].decode()
    tree_checkout(tree_sha)

def checkout_recur(hash, message):
    type, data = read_object(hash)
    data = data.decode()
    x = 0
    return_hash = -1
    indices = []
    while x != -1:
        x = data.find('\n', x+1, len(data)-1)
        if x != -1:
            indices.append(x)
    msg= data[indices[-1]+1:]
    msg = msg[:-1]
    if msg == message:
        return_hash = hash
    else:
        i = data.find('parent')
        if i != -1:
            parent_sha = data[i+7:i+47]
            return_hash = checkout_recur(parent_sha, message)
        else:
            return_hash = -1
    return return_hash


def tree_checkout(tree_sha):
    entries = read_tree(sha1 = tree_sha)
    for entry in entries:
        type, data = read_object(entry[2])
        file_path = entry[1]
        write_file(file_path, data)