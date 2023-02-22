from moviepy.editor import *
import math

clipVideo = VideoFileClip(r"C:\Users\vihaa\Python-Examples\VideoMaker\Clips\Bluey_S01E01_The Magic Xylophone.mp4")#.margin(10)
clipBack = VideoFileClip(r"C:\Users\vihaa\Python-Examples\VideoMaker\Clips\Untitled video - Made with Clipchamp.mp4")#.margin(10)

clipVideoDuration = clipVideo.duration - 25

numberOfClips = math.ceil(clipVideoDuration)

clipLengthMean = clipVideoDuration/numberOfClips

clipBack = clipBack.without_audio()

clipVideo = clipVideo.resize(.45)
print(clipVideoDuration)
print(numberOfClips)
print(clipLengthMean)


for clipsMade in range(math.ceil((numberOfClips/60))-1):
    clipBack = clipBack.subclip((clipsMade,0),(clipLengthMean*(clipsMade+1),0))
    clipVideo = clipVideo.subclip((clipsMade,25),(clipLengthMean*(clipsMade+1),25))

    final_clip = CompositeVideoClip([clipBack.set_position((0,0)),clipVideo.set_position((0,0))])

    final_clip.write_videofile(r"C:\Users\vihaa\Python-Examples\VideoMaker\Test\stacked_vid{}.mp4".format(clipsMade))
