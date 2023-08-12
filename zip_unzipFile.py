import zipfile
def zip_unzipFile(zipFilePath, whereToExtract):
	with zipfile.ZipFile(zipFilePath, 'r') as zip_ref:
		zip_ref.extractall(whereToExtract)