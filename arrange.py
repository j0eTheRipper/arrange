#!/usr/bin/env python3

from os import rename as mv
from os import listdir, mkdir
from os.path import isdir
from json import dump, load
import argparse


add_dir_help = '''set up a directory to add files to.
When this is used, --ext option has to be used, to specify
the extensions that goes in the new directory'''

ext_help = '''A space separated  of extensions that go into the new directory
specified using the add_dir option.
NOTE, this is not to be used alone. it has to be used with the --add-dir option.'''

parser = argparse.ArgumentParser(description='Arrange the given dir')
parser.add_argument('--dir', help='specify a directory to clean (default: Downloads)')
parser.add_argument('--add_dir', help=add_dir_help)
parser.add_argument('--ext', help=ext_help)
args = parser.parse_args()


class DIR:
	def __init__(self, path, extensions):
		self.path = path
		self.extensions = extensions
		self.extensions_file = None

	def get_existing_extensions(self):
		try:
			with open('.extensions.json') as extensions:
				self.extensions_file = load(extensions)
		except FileNotFoundError:
			self.extensions_file = dict()

	def extensions_setup(self):
		if self.path in self.extensions_file:
			self.extensions_file[self.path].extend(self.extensions)
		else:
			self.extensions_file[self.path] = self.extensions

		with open('.extensions.json', 'w') as extensions:
			dump(self.extensions_file, extensions)

	def dir_setup(self):
		self.get_existing_extensions()
		self.extensions_setup()

		if not isdir(self.path):
			mkdir(self.path)


class File:
	def __init__(self, path):
		self.path = path
		self.name = self.path.split('/')[-1]
		self.extension = self.path.split('.')[-1]
		self.destination = ''

	@staticmethod
	def get_extensions():
		with open('.extensions.json', 'r') as extensions:
			dir_ext = load(extensions)

		return dir_ext

	def determine(self):
		dir_ext = self.get_extensions()

		for directory, extensions in dir_ext.items():
			if self.extension in extensions:
				self.destination = directory
				break

	def move(self):
		mv(self.path, f'{self.destination}/{self.name}')

	def operate(self):
		self.determine()

		if self.destination != '':
			self.move()


def clean_dir(target_dir):
	dir_contents = listdir(target_dir)
	for file_ in dir_contents:
		file = File(f'{target_dir}/{file_}')
		file.operate()


# User commands
if args.dir:
	clean_dir(args.dir)
elif args.add_dir:
	if args.ext:
		ext = (args.ext.split())
		new_dir = DIR(args.add_dir, ext)
		new_dir.dir_setup()
	else:
		print("Please use --ext option to specify the new directory's extensions")
elif args.ext and not args.add_dir:
	print('Cannot use --ext alone! Refer to help for more')
else:
	clean_dir('Downloads')
