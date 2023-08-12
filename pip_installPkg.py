from proc_runCmd import proc_runCmd

def pip_installPkg( pkgNm ):
	proc_runCmd(['pip', 'install', pkgNm])