from os import mkdir, listdir, rmdir, rename, makedirs
from os.path import abspath


class DIR:
    def __init__(self, directory_path):
        self.dir_path = abspath(directory_path)
        self.dir_name = self.dir_path.split('/')[-1]
        self.dir_parent = '/'.join(self.dir_path.split('/')[:-1])

    def create_directory(self):
        try:
            mkdir(self.dir_path)
        except FileExistsError:
            pass

    def update_directory_path(self, new_path):
        self.dir_parent = f'{abspath(new_path)}/{self.dir_name}'

        try:
            rename(self.dir_path, self.dir_parent)
        except FileNotFoundError:
            print('Exception is being handled')
            makedirs(self.dir_parent)
        # finally:
            rename(self.dir_path, self.dir_parent)
