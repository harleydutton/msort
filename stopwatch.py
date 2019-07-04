from datetime import datetime as dt
mark = dt.now()
def lap():
	global mark
	elapsed = (dt.now()-mark).total_seconds()
	mark = dt.now()
	return elapsed