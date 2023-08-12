from deps_sublime_checkInstall import deps_sublime_checkInstall

def deps_subliem_setUserSetting():
	if deps_sublime_checkInstall() == False:
		print('[ERR] 서브라임이 설치되지 않음')
	with open('./tmp/sublime/Data/Packages/User/Preferences.sublime-settings', 'w') as f:
		f.write('{ "auto_complete": false, "ignored_packages":[], "save_on_focus_lost": true, "font_face": "D2Coding", "font_size": 9, }')

if __name__ == '__main__':
	deps_subliem_setUserSetting()