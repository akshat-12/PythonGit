# PythonGit
 A version control system built using python. PythonGit, or PyGit, currently supports local version control operations for a top-level directory with no subdirectories. PyGit uses no external libraries and is built purely on in-built python libraries. You'd need a unix-shell to run PyGit, so use WSL if you're a Windows user.

# About PyGit
 PyGit currently offers following arguements:
 1. init: Initialize a folder to a PyGit repository. (Folder should not exist beforehand).
 2. add: Add a file to the index.
 3. commit: Save the current index as a commit (also provide an author and a message).
 4. hash-file: A plumbing command. Use this to find the hash-value of any file.
 5. cat-file: Another plumbing command. Use this to display a file given its hash-value.
 6. logs: Pull out the commit logs.
 7. status: Check if the current index is same as the current working files or have the files changed.
 8. diff: Print the differences between files in the index and the working copies of the files.
 9. ls-files: List the files present in the index.
 10. checkout: Checkout a previous version of the project using the commit message.

# How to PyGit
 Initialize a repository using PyGit init.

 ![init](https://github.com/akshat-12/PythonGit/blob/main/images/init.PNG)

 Move into the newly created folder. You'll see a .pygit folder. Here's how the inside of it looks like.

 ![inside_dir](https://github.com/akshat-12/PythonGit/blob/main/images/pygit_dir.PNG)

 Create a file, let's say a.txt. Input some content into a.txt.

 ![createfile](https://github.com/akshat-12/PythonGit/blob/main/images/createfile.PNG)

 Add the a.txt to the index using PyGit add.

 ![add](https://github.com/akshat-12/PythonGit/blob/main/images/add.PNG)

 Commit the current index using PyGit commit.

 ![firstcommit](https://github.com/akshat-12/PythonGit/blob/main/images/firstcommit.PNG)

 Make some changes to working files. Change content of a.txt and add another file b.txt.

 ![changecontent](https://github.com/akshat-12/PythonGit/blob/main/images/changecontent.PNG)
 ![newfile](https://github.com/akshat-12/PythonGit/blob/main/images/newfile.PNG)

 Since the b.txt is not added to index yet, the ls-files will be same as before.

 ![newcheck](https://github.com/akshat-12/PythonGit/blob/main/images/newcheck.PNG)

 Check the status of files using PyGit status.

 ![status](https://github.com/akshat-12/PythonGit/blob/main/images/status.PNG)

 Check the differences between a.txt of the index and current a.txt using PyGit diff.

 ![diff](https://github.com/akshat-12/PythonGit/blob/main/images/diff.PNG)

 Add the new a.txt and b.txt to the index using PyGit add.

 ![secondadd](https://github.com/akshat-12/PythonGit/blob/main/images/secondadd.PNG)

 Commit this as well.

 ![secondcommit](https://github.com/akshat-12/PythonGit/blob/main/images/secondcommit.PNG)

 See the commit logs using PyGit logs.

 ![logs](https://github.com/akshat-12/PythonGit/blob/main/images/logs.PNG)

 Checkout the first commit using PyGit checkout

 ![checkout](https://github.com/akshat-12/PythonGit/blob/main/images/checkout.PNG)

 ![checkoutcheck](https://github.com/akshat-12/PythonGit/blob/main/images/checkoutcheck.PNG) 

# Literature

I read about the internal workings of Git from around the internet. There are some very good sources available out there. I've compiled my learning into a GitInternals.pdf. You can find this inside the literature folder.

The current project PyGit is also explained inside PyGit.pdf. You can find this too inside the literature folder.

# Future Scope

Currently, there are two more functionaltites I'm trying to implement to this project.

1. Updating this project to work for subdirectories as well, and not just top-level directories.
2. Implementing functionalities to add commands to push the project to GitHub/BitBucket.
