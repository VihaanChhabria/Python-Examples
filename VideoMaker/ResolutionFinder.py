# Import everything needed to edit video clips
from moviepy.editor import *
	
# loading video dsa gfg intro video
clip = VideoFileClip(r"C:\Users\vihaa\Python-Examples\VideoMaker\Clips\Subway Surfers - 1 Hour Gameplay High Score _ ANDROID.mp4")
	
# getting only first 5 seconds
clip = clip.subclip(0, 5)

# getting clip size
value = clip.size

# printing size
print("Clip Size ", end = " : ")
print(value)


# displaying new clip
#clip.ipython_display(width = 420)
