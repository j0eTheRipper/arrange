from setuptools import setup


setup(
        name='arrange',
        version='3.0.0',
        description='Move files in the downloads directory to their appropriate directory.',
        url='https://github.com/j0eTheRipper/arrange',
        author='j0eTheRipper',
        author_email='j0eTheRipper0010@gmail.com',
        packages=['engine', 'engine.DIR', 'engine.File', 'engine.Extensions'],
        py_modules=['arrange', 'engine.DIR.DIR', 'engine.File.File', 'engine.Extensions.Extensions'],
        package_dir={'':'src'}
)

