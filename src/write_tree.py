from src.hash_object import hash_object
from src.index import read_index

def write_tree():
    tree_entries = []
    for entry in read_index():
        assert '/' not in entry.path, 'currently only supports a single, top-level directory'
        mode_path = '{:o} {}'.format(entry.mode, entry.path).encode()
        tree_entry = mode_path + b'\x00' + entry.sha1
        tree_entries.append(tree_entry)
    return hash_object(b''.join(tree_entries), 'tree')