from app import app

@app.route('/')
@app.route('/index')
def index():
	cpuTempFile = open('/sys/class/thermal/thermal_zone0/temp', 'r')
	cpuTemp = float(cpuTempFile.read()) / 1000
	cpuTempFile.close()
	msg = str(cpuTemp)
	return msg
