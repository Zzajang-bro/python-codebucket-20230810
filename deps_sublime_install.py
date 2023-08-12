import traceback
try:
	from req_downloadWebResource_toTmpDirectory import req_downloadWebResource_toTmpDirectory
	from zip_unzipFile import zip_unzipFile
	from file_makeDirIfNotExist import file_makeDirIfNotExist
	def deps_sublime_download():
		url = 'https://download.sublimetext.com/sublime_text_build_4152_x64.zip'
		file_makeDirIfNotExist('./tmp/sublime')
		req_downloadWebResource_toTmpDirectory(url, 'sublime/sublime.zip')
		zip_unzipFile('./tmp/sublime/sublime.zip', './tmp/sublime')
	if __name__ == '__main__':
		deps_sublime_download()
except:
	print(traceback.format_exc())
	input()