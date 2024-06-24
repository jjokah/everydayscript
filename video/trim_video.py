"""
Trims a clip from a video.

Parameters:
path (str): The path to the video to be trimmed.
options (dict): A dictionary of options to pass to yt_dlp for downloading the video.
start_time (str): The start time of the desired clip in HH:MM:SS format.
end_time (str): The end time of the desired clip in HH:MM:SS format.

Functionality:
Loads a video using VideoFileClip.
Extracts the clip from start_time to end_time.
Resizes the height of the clip to 360 pixels.
Sets the FPS to 24.
Writes the clipped video to compressed_clip.mp4.

Requirements:
pip install moviepy
"""
from moviepy.editor import VideoFileClip

# Load the video
video = VideoFileClip("video.mp4")

# Define the start and end times of the desired clip in seconds
start_time = "00:09:27"
end_time = "00:09:55"

# Extract the desired clip
clip = video.subclip(start_time, end_time)

# Set the output video parameters
# clip = clip.resize(height=360)  # resize the height to 360 pixels

# Write the output video
clip.write_videofile("clip.mp4")
