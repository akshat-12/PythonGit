import sys
import stat
from src.read_tree import read_tree
from src.object_utilities import read_object

def cat_file(mode, sha1_prefix):
    obj_type, data = read_object(sha1_prefix)
    if mode in ['commit','tree','blob']:
        if obj_type != mode:
            raise ValueError('expected object type {}, got {}'.format(mode, obj_type))
        sys.stdout.buffer.write(data)
    elif mode == 'size':
        print(len(data))
    elif mode == 'type':
        print(obj_type)
    elif mode == 'pretty':
        if obj_type in ['commit', 'blob']:
            sys.stdout.buffer.write(data)
        elif obj_type == 'tree':
            for mode, path, sha1 in read_tree(data=data):
                type_str = 'tree' if stat.S_ISDIR(mode) else 'blob'
                print('{:06o} {} {}\t{}'.format(mode, type_str, sha1, path))
        else:
            assert False, 'unhandled object type {!r}'.format(obj_type)
    else:
        raise ValueError('unexpected mode {!r}'.format(mode))