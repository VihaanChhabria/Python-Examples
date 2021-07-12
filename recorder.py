#Records a sound file of .wav of your voice
import sounddevice as sd
from scipy.io.wavfile import write

fs = 44100  # Sample rate
seconds = 2 # Duration of recording

myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()  # Wait until recording is finished
write('AAA.wav', fs, myrecording)  # Save as WAV file 