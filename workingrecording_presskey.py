#!/usr/bin/env python
#!/usr/bin/env python3
import struct
import alsaaudio
import thread
from fileSendClient import fileSendClientMain

recording = True

def StopRecording():
	recording = False

def input_thread(list):
	#raw_input("Press enter to stop recording")
	while recording:
		pass
	list.append(None)


def WorkingRecording():

	sound_out = alsaaudio.PCM()  
	# open default sound output
	sound_out.setchannels(1)
	# use only one channel of audio (aka mono)
	#sound_out.setperiodsize(5) 
	# buffer size, default is 32
	sound_out.setrate(8000)

	sound_in = alsaaudio.PCM(type=alsaaudio.PCM_CAPTURE)
	# default recording device
	sound_in.setchannels(1)
	# use only one channel of audio (aka mono)
	#sound_in.setperiodsize(5) 
	# buffer size, default is 32
	sound_in.setrate(8000)
	sound_in.setperiodsize(160)

	output_filename = "test_recording.wav"

	#total_length = 0
	list = []
	wf = open(output_filename, 'wb')
	thread.start_new_thread(input_thread, (list, ))
	while not list:
	    sample_length, sample = sound_in.read()
	    #print("length " + str(sample_length))
	    #total_length += sample_length
	    sound_out.write(sample)
	    wf.write(sample)

	wf.close()

	fileSendClientMain()
	    
	print("=========================================================")
	print("Recording complete, file created: " + output_filename)
	print("=========================================================")

	thread.exit()

if __name__ == '__main__':
    WorkingRecording()
