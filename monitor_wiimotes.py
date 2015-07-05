import subprocess
import time


def monitor_wiimotes():
	failed_once = False
	while True:
		running = emulator_running()
		if failed_once and not running:
			subprocess.call(['killall', 'wminput'])
		else: 
			failed_once = not running

		time.sleep(60)

# if no emulators are running, kill wiimote connections
def emulator_running():
	try:
		es_pid = subprocess.check_output(['pgrep', '-f', '/opt/retropie/supplementary/emulationstation/emulationstation'])
		es_pid = es_pid.rstrip() # remove newline
	except:
		# es isn't running
		return False
	else: 
		try:
			childen = subprocess.check_output(['pgrep', '-cP', es_pid])
		except:
			# no children
			return False
		else: 
			return True	

monitor_wiimotes()

