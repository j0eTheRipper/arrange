from os import listdir

from arrange import ext, home, json_file_path
from classes.DIR import DIR
from classes.File import File


def setup_json():
    print("This is the first time for the program to run...")
    print("adding extensions to json file...")
    ext.add_extensions(f'{home}/Pictures', {'jpg', 'jpeg', 'png', 'gif'})
    ext.add_extensions(f'{home}/Documents', {'doc', 'docx', 'pdf', 'csv', 'xlsx'})
    ext.add_extensions(f'{home}/Videos', {'mp4', 'mkv'})
    ext.add_extensions(f'{home}/Music', {'mp3'})
    ext.write_json_file()
    print("done!")
    print('Cleaning your Downloads folder...')
    clean_directory(f'{home}/Downloads')
    print('DONE')


def clean_directory(directory):
    for file in listdir(directory):
        file = f'{directory}/{file}'
        file = File(file, json_file_path)
        file.main()


def setup(directory, extensions):
    directory = setup_dir(directory)
    extensions_set = setup_extensions_set(extensions)
    return directory, extensions_set


def setup_extensions_set(extensions):
    extensions = extensions.split('-')
    return set(extensions)


def setup_dir(directory):
    directory = DIR(directory)
    directory.create_directory()
    return directory
