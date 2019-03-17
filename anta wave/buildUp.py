import subprocess
import pyaudio
import time

def start():
	chunk = 1024
	while(isOpen):
		p = pyaudio.PyAudio()
		stream = p.open( format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=chunk )
		data = stream.read(chunk)
		print(data)
		time.sleep(5)

def isOpen():
	# Check if linux of mac later
	cmd = 'tasklist'
	proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
	if('spotify.exe' in proc):
		return True
	return False

start()