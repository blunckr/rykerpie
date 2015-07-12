import os
import subprocess
from time import sleep

def get_next_player_number():
	devs = os.listdir('/dev/input')
	
	for i in range(0, 4):		
		if 'js' + str(i) not in devs:
			return str(i + 1)

	return None

def create_config_file(player):
	template_file = open('/home/pi/rykerpie/gamepad')
	content = template_file.read()
	template_file.close()

	tmp_dir = '/home/pi/rykerpie/tmp'
	if not os.path.exists(tmp_dir):
		os.makedirs(tmp_dir)

	new_file = open('/home/pi/rykerpie/tmp/custom_gamepad' + player, 'w')
	new_file.write(content)
	new_file.write('\n')
	new_file.write('Plugin.led.Led' + player + ' = 1')
	new_file.write('\n')
	new_file.close()

def connect_wiimote():
	player = get_next_player_number()
	if player is None:
		return

	create_config_file(player)

	process = subprocess.Popen(['wminput', '-c', '/home/pi/rykerpie/tmp/custom_gamepad' + player],
	                                                    stdout=subprocess.PIPE)
	
	sleep(10)

def scan_bluetooth():
	while True:
		out = subprocess.check_output(['hcitool', 'scan', '--flush'])
		if 'Nintendo' in out:
			connect_wiimote()
		
		sleep(3)
	
scan_bluetooth()
