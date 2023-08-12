import os

def file_makeDirIfNotExist(nm):
	if not os.path.isdir(nm):
		os.mkdir(nm)