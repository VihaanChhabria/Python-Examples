import wave 

file1 = wave.open('Minecraft_Fishing_Sound.wav', 'r')
file2 = wave.open('Minecraft_Fishing_Sound.wav', 'r')

if file1.readframes(-1) == file2.readframes(-1):
    print("equal")
else:
    print("not equal")