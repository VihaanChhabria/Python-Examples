
from moviepy.editor import *
import math

clip11 = VideoFileClip(r"C:\Users\vihaa\Python-Examples\VideoMaker\Clips\Bluey_S01E01_The Magic Xylophone.mp4")#.margin(10)
#clip21 = VideoFileClip(r"C:\Users\vihaa\Python-Examples\VideoMaker\Clips\Untitled video - Made with Clipchamp.mp4")#.margin(10)

print(math.floor(clip11.duration))

#clip21 = clip21.without_audio()

#duration = 10

#clip21 = clip21.subclip((0,0),(0,10))
#clip11 = clip11.subclip((0,25),(0,35))

#clip11 = clip11.resize(.45)
  


#final_clip = CompositeVideoClip([clip21.set_position((0,0)),clip11.set_position((0,0))])

#final_clip.write_videofile("stacked_vidTest.mp4")