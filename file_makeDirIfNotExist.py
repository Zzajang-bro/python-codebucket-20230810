import os

def file_makeDirIfNotExist(path):
	from pathlib import Path
	Path(path).mkdir(parents=True, exist_ok=True)
