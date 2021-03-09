# description
Moves files to thier suitable directory according the the file's extension

## usage
When the executed without any arguments, it cleans the downloads folder.

if you wanna clean another directory other than the downloads, you should use the `--dir` option:

`python arrange.py --dir '/full/path/to/dir/'`

if you wanna set up a new directory to add un cleaned files to, you should use the `--add_dir` option specifying the path to the new directory
along with the `--ext` option specifying the extensions that go in to the directory as a space separated list.

`python arrange.py --add_dir '/full/path/to/dir' --ext ext1 ext2 ...`

If you want to clean all the folders in the home directory, use the `--all`
flag.
