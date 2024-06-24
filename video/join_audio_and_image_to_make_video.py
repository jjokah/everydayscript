from moviepy.editor import *

# Load the audio file
audio = AudioFileClip("audio.mp3")

# Cut a portion of the audio (e.g. from 10 seconds to 30 seconds)
audio_cut = audio.subclip(0, 59)

# Load the image file
image = ImageClip("image.jpg")

# Set the duration of the video to be the same as the cut audio
duration = audio_cut.duration

# Create a video clip from the image with the same duration as the cut audio
video = image.set_duration(duration)

# Add the cut audio to the video
video.audio = audio_cut

# Write the video to a file
video.write_videofile("output.mp4", fps=24)
