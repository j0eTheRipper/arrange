from os import listdir, rmdir
from .DIR import DIR


def test_directory_creation():
    remove_existing_directory('abc')

    new_directory = DIR('abc')
    new_directory.create_directory()

    assert 'abc' in listdir('.')
    remove_existing_directory('abc')


def test_dir_ancestor():
    remove_existing_directory('abc')
    new_directory = DIR('abc')

    assert new_directory.dir_ancestors == {'/home/j0e/Projects/Python/automation_scripts/arrange/classes',
                                           '/home/j0e/Projects/Python/automation_scripts/arrange',
                                           '/home/j0e/Projects/Python/automation_scripts',
                                           '/home/j0e/Projects/Python',
                                           '/home/j0e/Projects'}


def remove_existing_directory(directory):
    if directory in listdir('.'):
        rmdir(directory)

