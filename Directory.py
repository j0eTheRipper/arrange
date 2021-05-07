from os import mkdir
from os.path import isdir
from json import dump, load


class DIR:
	"""Creates the directory and adds the extensions to the extensions list."""
	def __init__(self, path, extensions):
		self.path = path
		self.new_extensions = set(extensions)
		self.dir_to_ext = None

	def get_dir_to_ext(self):
		"""Gets the Directory ==> Extensions dictionary from the json file."""
		try:
			with open('.extensions.json') as extensions:
				self.dir_to_ext = load(extensions)
		except FileNotFoundError:
			self.dir_to_ext = dict()

	def add_extensions(self):
		"""Adds the extensions to the Directory's list in the json file."""
		if self.path in self.dir_to_ext:
			existing_extensions = set(self.dir_to_ext[self.path])
			self.dir_to_ext[self.path] = existing_extensions | self.new_extensions
		else:
			self.dir_to_ext[self.path] = self.new_extensions

		with open('.extensions.json', 'w') as extensions:
			dump(self.dir_to_ext, extensions)

	def dir_setup(self):
		self.get_dir_to_ext()
		self.add_extensions()

		if not isdir(self.path):
			mkdir(self.path)
