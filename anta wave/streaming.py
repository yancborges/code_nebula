import pyaudio
import numpy as np
import sounddevice as sd
from scipy.fftpack import fft

CHUNK = 2048
# Get value from OS
RATE = 44100
FORMAT = pyaudio.paInt16
CHANNELS = 1

NUMBER_OF_LEDS = 10

def get_bars(value):
	i = int(value)
	
	abs_value = (100*i/RATE)*2
	lit = ((NUMBER_OF_LEDS*abs_value)/100)
	bar = '#'*int(lit)
	return (lit,bar)

def display_spectrum(value):
	
	i_leds,v_leds = get_bars(value)

	print('%-8d %-30s [%d/%d]' %(value,v_leds,i_leds,NUMBER_OF_LEDS))

def play(stream):
	data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
	peak=np.average(np.abs(data))*2
	#peak = np.amax(np.abs(data))*2
	bars="#"*int(50*peak/2**16)
	#print("%05d %s"%(peak,bars))
	return peak

def gather(op):
	
	p=pyaudio.PyAudio()

	if(op == 'out'):
		stream=p.open(format=FORMAT,channels=CHANNELS,rate=RATE,input=True,frames_per_buffer=CHUNK)
	else:
		SPEAKERS = p.get_default_output_device_info()['index']
		
		host_info = p.get_host_api_info_by_index(0)    
		device_count = host_info.get('deviceCount')
		devices = []

		# iterate between devices:
		print(p.get_device_info_by_index(3))

		#stream = p.open(format=FORMAT,channels=CHANNELS,rate=RATE,input=True,frames_per_buffer=CHUNK,input_host_api_specific_stream_info=SPEAKERS)
		stream = p.open(format=FORMAT,channels=0,rate=RATE,input=True,frames_per_buffer=CHUNK,input_device_index=SPEAKERS)

	if(stream.is_stopped()):
		stream.start_stream()

	try:
		while(True):
			display_spectrum(play(stream))
	except Exception as e:
		print(e)

	stream.stop_stream()
	if(stream.is_active()):
		stream.close()
	p.terminate()
	

gather('out')


	