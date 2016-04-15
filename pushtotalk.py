#!/usr/bin/env python
#!/usr/bin/env python3
import struct
import alsaaudio

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

while True:
    sample_lenght, sample = sound_in.read()
    sound_out.write(sample)
