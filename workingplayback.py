import struct
import alsaaudio

f = open ("test_recording.wav")

sound_out = alsaaudio.PCM()

sound_out.setchannels(1)
# use only one channel of audio (aka mono)
#sound_out.setperiodsize(5) 
# buffer size, default is 32
sound_out.setrate(8000)

sound_out.setperiodsize(160)

data = f.read(160)
while data:
	sound_out.write(data)
	data = f.read(160)
