from json import load
from os import rename as mv


class File:
	def __init__(self, path):
		self.path = path
		self.name = self.path.split('/')[-1]
		self.extension = self.path.split('.')[-1]
		self.destination = ''

	@staticmethod
	def get_extensions():
		with open('.extensions.json', 'r') as extensions:
			dir_ext = load(extensions)

		return dir_ext

	def determine(self):
		dir_ext = self.get_extensions()

		for directory, extensions in dir_ext.items():
			if self.extension in extensions:
				self.destination = directory
				break

	def move(self):
		mv(self.path, f'{self.destination}/{self.name}')

	def operate(self):
		self.determine()

		if self.destination != '':
			self.move()
