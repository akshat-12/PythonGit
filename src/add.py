import enum
import os
import operator
from src.index import read_index, IndexEntry, write_index
from src.hash_object import hash_object
from src.file_utilities import read_file

class ObjectType(enum.Enum):
    commit = 1
    tree = 2
    blob = 3

def add(paths):
    all_entries = read_index()
    entries = [e for e in all_entries if e.path not in paths]
    for path in paths:
        sha1 = hash_object(read_file(path), 'blob')
        st = os.stat(path)
        flags = len(path.encode())
        assert flags < (1 << 12)
        entry = IndexEntry(
                int(st.st_ctime), 
                0, 
                int(st.st_mtime), 
                0, 
                st.st_dev,
                0,
                #st.st_ino, 
                st.st_mode, 
                st.st_uid, 
                st.st_gid, 
                st.st_size,
                bytes.fromhex(sha1), 
                flags, 
                path)
        entries.append(entry)
    entries.sort(key=operator.attrgetter('path'))
    write_index(entries)