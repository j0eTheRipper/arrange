#!/usr/bin/env python3

from os.path import isfile, expanduser
from argparse import ArgumentParser
from sys import exit
from classes.Extensions import Extensions
from setup_functions import setup_json, clean_directory, setup, setup_dir

parser = ArgumentParser(description='Arrange the given directory')
parser.add_argument('-d', '--dir', help='For specifying a directory')

parser.add_argument('-ae', '--add_ext',
                    help='add a hyphen separated list of filetypes to a directory (specified using -d)')
parser.add_argument('-re', '--remove_ext',
                    help='Omit a hyphen separated list of filetypes from being cleaned (specified using -d)')
parser.add_argument('-r', '--remove_directory',
                    help='Omit the given directory having filetypes added to')
parser.add_argument('-c', '--clean_directory',
                    help='Clean the given directory')

args = parser.parse_args()

home = expanduser('~')
json_file_path = f'{home}/.config/arrange.json'
ext = Extensions(json_file_path)


def main():
    global args

    if not isfile(json_file_path):
        setup_json()

    if args.add_ext:
        if args.dir:
            directory, extensions_set = setup(args.dir, args.add_ext)

            ext.add_extensions(directory, extensions_set)
            ext.write_json_file()
        else:
            print('Specify directory using -d argument')
            exit()
    elif args.remove_ext:
        if args.dir:
            directory, extensions_set = setup(args.dir, args.remove_ext)

            ext.remove_extensions(directory, extensions_set)
            ext.write_json_file()
        else:
            print('Specify directory using -d argument')
            exit()
    elif args.remove_directory:
        directory = setup_dir(args.remove_directory)

        ext.remove_directory(directory)
        ext.write_json_file()
    elif args.clean_directory:
        directory = setup_dir(args.clean_directory)

        clean_directory(directory)
    else:
        clean_directory(f'{home}/Downloads')


if __name__ == '__main__':
    main()
