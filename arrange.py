#!/usr/bin/env python3

from os import listdir
from os.path import abspath, isfile
from argparse import ArgumentParser
from sys import exit
from classes.Extensions import Extensions
from classes.File import File
from classes.DIR import DIR


add_dir_help = 'Specify a directory for the program to put files into'

ext_help = 'A hyphen (-) separated list of file extensions that go into the directory specified by the --add_dir option'

parser = ArgumentParser(description='Arrange the given directory')
parser.add_argument('--dir', help='specify a directory to clean (default: Downloads)')
parser.add_argument('--add_dir', help=add_dir_help)
parser.add_argument('--del_dir', help='Omit the directory with its extensions from the cleaning process')
parser.add_argument('--ext', help=ext_help)
args = parser.parse_args()

home = abspath(__name__).split('/')[:3:]
home = '/'.join(home)
json_file_path = f'{home}/.config/arrange.json'


def clean_dir(target_dir):
    target_dir = abspath(target_dir)
    dir_contents = listdir(target_dir)
    for file_ in dir_contents:
        file = File(f'{target_dir}/{file_}', json_file_path)
        file.main()


def update_json(directory, extensions):
    extensions = set(extensions.split('-'))
    directory = abspath(directory)
    Extensions(directory, extensions, json_file_path)
    new_dir = DIR(directory)
    new_dir.create_directory()


if not isfile(json_file_path) and (args.ext and args.add_dir):
    update_json(args.add_dir, args.ext)
else:
    print("""Please specify the extensions:
    ./arrange --add_dir [path to directory] --ext exts-to-add-to-directory.""")
    exit()

# User commands
if args.dir:
    try:
        clean_dir(args.dir)
    except FileNotFoundError:
        print('Please enter a valid directory.')
elif args.add_dir:
    if args.ext:
        update_json(args.add_dir, args.ext)
    else:
        print("Please use --ext option to specify the new directory's extensions")
elif args.ext and not args.add_dir:
    print('Please use --add_dir to specify the directory for the extensions')
else:
    clean_dir(f'{home}/Downloads')
