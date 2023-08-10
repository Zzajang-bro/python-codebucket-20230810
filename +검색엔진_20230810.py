import os
import traceback
try:
	def search(query):
		for fl in os.listdir():
			if not os.path.isfile(fl):
				continue
			with open(fl, 'r', encoding='utf8') as f:
				dat = f.read()
			if query in dat:
				print(fl)


	while True:
		search(input('검색어: '))
except:
	print(traceback.format_exc())
	input()