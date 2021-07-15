from json import load
from os import rename as mv


class File:
    def __init__(self, file_path, json_file_path):
        self.file_path = file_path
        self.file_name = self.file_path.split('/')[-1]
        self.file_extension = self.file_path.split('.')[-1]
        self.json_file = json_file_path
        self.destination = ''

    def get_extensions(self):
        """Gets directory to extension dictionary from the json file_path"""
        with open(self.json_file, 'r') as extensions:
            dir_ext = load(extensions)

        return dir_ext

    def determine(self):
        """determines where the given file_path would go"""
        dir_ext = self.get_extensions()

        for directory, extensions in dir_ext.items():
            if self.file_extension in extensions:
                self.destination = directory
                break

    def move(self):
        """moves the given file_path to the specified destination."""
        mv(self.file_path, f'{self.destination}/{self.file_name}')

    def operate(self):
        self.determine()

        if self.destination != '':
            self.move()
