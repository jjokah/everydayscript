from moviepy.editor import VideoFileClip


# Load the video file
video = VideoFileClip("video.mp4")

# Extract the audio from the video
audio = video.audio

# Write the audio to a file
audio.write_audiofile("audio.mp3")
