import traceback
try:
	import subprocess
	import sys

	def proc_runCmd( cmdList ):
		print(f'runCmd: {cmdList}')
		subprocess.Popen(cmdList, stdout=sys.stdout, stderr=sys.stdout)

except:
	print(traceback.format_exc())
	input()