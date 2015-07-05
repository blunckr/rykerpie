import os
import re
import subprocess
import time

def get_next_player_number():
	devs = os.listdir('/dev/input')
	js_matcher = re.compile('^js')
	players = 1
	for dev in devs:
		if js_matcher.match(dev):
			players += 1
	
	return players

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

# recursively calls itself until it fails to find one
def connect_wiimotes():
	player = get_next_player_number()
	create_config_file(str(player))

	process = subprocess.Popen(['wminput', '-c', '/home/pi/rykerpie/tmp/custom_gamepad' + str(player)],
	                           stdout=subprocess.PIPE)
	
	time.sleep(10)
	result = process.poll()
	if result == None: # no bad exit code
		connect_wiimotes()
