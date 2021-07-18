#!/usr/bin/env python3

from os import listdir
from os.path import abspath, isfile
from argparse import ArgumentParser
from sys import exit
from classes.Extensions import Extensions
from classes.File import File
from classes.DIR import DIR


parser = ArgumentParser(description='Arrange the given directory')
parser.add_argument('--dir', help='specify a directory to be arranged (default: Downloads)')
parser.add_argument('--set_dir', help='Set a directory to add filetypes to')
parser.add_argument('--unset_dir', help='Prevent directory from being added files to using the program')
parser.add_argument('--ext', help='Filetype extensions to add to the directory specified using the --set-dir option')
parser.add_argument('--remove_ext', help='Prevent filetype extensions from going in a directory')
args = parser.parse_args()

home = abspath(__name__).split('/')[:3:]
home = '/'.join(home)
json_file_path = f'{home}/.config/arrange.json'
