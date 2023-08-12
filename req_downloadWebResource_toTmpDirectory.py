import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from urllib import request
from file_isFileExist import file_isFileExist
from file_makeDirIfNotExist import file_makeDirIfNotExist

def req_downloadWebResource_toTmpDirectory(url, nm):
	file_makeDirIfNotExist('./tmp')
	filePath = f'./tmp/{nm}'
	if not file_isFileExist(filePath):
		request.urlretrieve(url, filePath)