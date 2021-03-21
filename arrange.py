#!/usr/bin/env python3

from os import listdir
from os.path import abspath
from argparse import ArgumentParser

from classes.DIR import DIR
from classes.File import File

add_dir_help = '''set up a directory to add files to.
When this is used, --ext option has to be used, to specify
the extensions that goes in the new directory'''

ext_help = '''A space separated  of extensions that go into the new directory
specified using the add_dir option.
NOTE, this is not to be used alone. it has to be used with the --add-dir option.'''

parser = ArgumentParser(description='Arrange the given dir')
parser.add_argument('--dir', help='specify a directory to clean (default: Downloads)')
parser.add_argument('--add_dir', help=add_dir_help)
parser.add_argument('--ext', help=ext_help)
args = parser.parse_args()

home = abspath(__name__).split('/')[:3:]
home = '/'.join(home)


def clean_dir(target_dir):
	dir_contents = listdir(target_dir)
	for file_ in dir_contents:
		file = File(f'{target_dir}/{file_}', f'{home}/.config')
		file.operate()


# User commands
if args.dir:
	try:
		clean_dir(args.dir)
	except FileNotFoundError:
		print('Please enter a valid directory.')
elif args.add_dir:
	if args.ext:
		ext = args.ext.split('-')
		new_dir = DIR(args.add_dir, ext, f'{home}/.config')
		new_dir.dir_setup()
	else:
		print("Please use --ext option to specify the new directory's extensions")
elif args.ext and not args.add_dir:
	print('Cannot use --ext alone! Refer to help for more')
else:
	clean_dir(f'/home/j0e/Downloads')
