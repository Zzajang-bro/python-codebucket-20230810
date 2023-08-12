import traceback
import subprocess
try:
	import os
	from proc_runCmd import proc_runCmd

	def deps_sublime_execute():
		print(fr'{os.getcwd()}\tmp\sublime\subl.exe')
		#os.startfile(fr'{os.getcwd()}\tmp\sublime\sublime_text.exe')
		#subprocess.call(['./tmp/sublime/sublime_text.exe'])
		subprocess.call(['./tmp/sublime/sublime_text.exe', os.getcwd()])

	if __name__ == '__main__':
		deps_sublime_execute()
		input()
except:
	print(traceback.format_exc())
	input()