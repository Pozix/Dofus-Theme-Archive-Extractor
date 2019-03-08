import os
import re
import zipfile
import hashlib
import struct
import pathlib
import xml.etree.ElementTree as ElT
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad

KEY = bytearray([123, 174, 87, 35, 78, 45, 94, 243, 78, 222, 147, 12, 47, 171, 251, 87])
theme_folder_path = 'C:/Users/A/AppData/Roaming/Dofus/ui/themes'
theme_download_path = 'C:/Users/A/AppData/Roaming/Dofus/ui/dll'


class Theme(object):
	def __init__(self, path):
		self._path = pathlib.Path(path).as_uri()
		self._padded = pad(struct.pack('>H', len(self._path)) + bytearray(self._path, 'utf-8'), len(KEY))
		self.hash = hashlib.md5(AES.new(KEY, AES.MODE_ECB).encrypt(self._padded)).hexdigest()


collection = os.listdir(theme_download_path)

for x in collection:
	m = re.search('^(.*)(.zip)+$', x)
	if m:
		zip_path = '{}/{}'.format(theme_download_path, m.group())
		theme_name = m.group(1)
		data_archive = zipfile.ZipFile(zip_path, 'r')
		data = data_archive.read('{}.dt'.format(theme_name))
		root = ElT.fromstring(data)
		folder_name = "{}_{}".format(root.find("./author").text, root.find("./name").text)
		theme_path = '{}/{}'.format(theme_folder_path, folder_name)

		if os.path.exists(theme_path):
			print('Folder found for theme: {}\nSkipping'.format(folder_name))
		if not os.path.exists(theme_path):
			print('Folder not found for theme: {}\nCreating it'.format(folder_name))
			os.makedirs(theme_path)
			if os.path.exists(theme_path):
				file = open(theme_path + '/' + Theme(theme_path).hash + '.txt', 'w+')
				file.close()
				data_archive.extractall(theme_path)
		data_archive.close()
