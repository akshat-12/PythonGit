import os
from index import read_index
from hash_object import hash_object
from file_utilities import read_file

def get_status():
    paths = set()
    for root, dirs, files in os.walk("."):
        dirs[:] = [d for d in dirs if d != '.pygit']
        for file in files:
            path = os.path.join(root, file)
            if path.startswith('./'):
                path = path[2:]
            paths.add(path)
    entries_by_path = {e.path: e for e in read_index()}
    entry_paths = set(entries_by_path)
    changed = {p for p in (paths & entry_paths) if hash_object(read_file(p), 'blob', write=False) != entries_by_path[p].sha1.hex()}
    new = paths - entry_paths
    deleted = entry_paths - paths
    return (sorted(changed), sorted(new), sorted(deleted))

def status():
    changed, new, deleted = get_status()
    if changed:
        print('changed files:')
        for path in changed:
            print('   ', path)
    if new:
        print('new files:')
        for path in new:
            print('   ', path)
    if deleted:
        print('deleted files:')
        for path in deleted:
            print('   ', path)