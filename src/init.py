import os
import configparser
from src.file_utilities import write_file

def init(repo):
    os.mkdir(repo)
    os.mkdir(os.path.join(repo, '.pygit'))
    for name in ['objects', 'refs', 'refs/heads', 'refs/tags', 'branches']:
        os.mkdir(os.path.join(repo, '.pygit', name))
    write_file(os.path.join(repo, '.pygit', 'HEAD'),
               b'ref: refs/heads/master')
    with open(os.path.join(repo, ".pygit","description.txt"), "w") as f:
        f.write("Unnamed repository; edit this file 'description' to name the repository.\n")
    with open(os.path.join(repo, ".pygit","config"), "w") as f:
        config = repo_default_config()
        config.write(f)
    print('initialized empty repository: {}'.format(repo))

def repo_default_config():
    ret = configparser.ConfigParser()

    ret.add_section("core")
    ret.set("core", "repositoryformatversion", "0")
    ret.set("core", "filemode", "false")
    ret.set("core", "bare", "false")
    return ret