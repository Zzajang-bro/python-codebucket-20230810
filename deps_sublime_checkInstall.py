import traceback
try:
	from file_isFileExist import file_isFileExist

	def deps_sublime_checkInstall():
		return file_isFileExist('./tmp/sublime/sublime_text.exe')

	if __name__ == '__main__':
		print(deps_sublime_checkInstall())
		input()
except:
	print(traceback.format_exc())
	input()