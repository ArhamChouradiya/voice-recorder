import sounddevice as sd
import wavio
from scipy.io.wavfile import write


fs = 44100 
seconds = 3 

myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()
write('output.wav', fs, myrecording)

#wavio.write('output.wav',myrecording, fs, sampwidth=1)
