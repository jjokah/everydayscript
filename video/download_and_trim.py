"""
Downloads a YouTube video and extracts a clip from it.

Parameters:
url (str): The URL of the YouTube video to download.
options (dict): A dictionary of options to pass to yt_dlp for downloading the video.
start_time (str): The start time of the desired clip in HH:MM:SS format.
end_time (str): The end time of the desired clip in HH:MM:SS format.

Functionality:
Uses yt_dlp to download the video from the given URL.
Loads the downloaded video using VideoFileClip.
Extracts the clip from start_time to end_time.
Resizes the height of the clip to 360 pixels.
Sets the FPS to 24.
Writes the clipped video to compressed_clip.mp4.

Requirements:
pip install yt-dlp
pip install moviepy
"""
import yt_dlp
from moviepy.editor import VideoFileClip

# Download the Video
url = "https://www.youtube.com/clip/UgkxvTnUj73ltQ3gG6ZNHcsjh1CnYq5013at"
options = {
    "format": "bestvideo[height<=360]+bestaudio/best[height<=360]",
    "outtmpl": "video.mp4",
}
with yt_dlp.YoutubeDL(options) as ydl:
    ydl.download([url])


# Load the video
video = VideoFileClip("video.mp4")

# Define the start and end times of the desired clip in seconds
start_time = "00:00:00"
end_time = "00:00:11"

# Extract the desired clip
clip = video.subclip(start_time, end_time)

# Set the output video parameters
# clip = clip.resize(height=360)  # resize the height to 360 pixels

# Write the output video
clip.write_videofile("clip.mp4")
