from json import load
from os import rename as mv


class File:
	def __init__(self, path):
		self.path = path
		self.name = self.path.split('/')[-1]
		self.extension = self.path.split('.')[-1]
		self.destination = ''

	@staticmethod
	def get_directory_extension_dict():
		"""Just look at the name for god's sake!!"""
		with open('.extensions.json') as extensions:
			dir_ext = load(extensions)

		return dir_ext

	def find_appropriate_directory(self):
		dir_ext = self.get_directory_extension_dict()

		for directory, extensions in dir_ext.items():
			if self.extension in extensions:
				self.destination = directory
				break

	def move(self):
		mv(self.path, f'{self.destination}/{self.name}')

	def operate(self):
		self.find_appropriate_directory()

		if self.destination != '':
			self.move()
