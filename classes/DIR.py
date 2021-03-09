from json import load, dump
from os import mkdir
from os.path import isdir


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