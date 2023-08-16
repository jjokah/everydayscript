"""
Extracts audio from a video,
transcribes the audio using Whisper,
and saves the transcription as TXT and SRT

Requirements:
sudo apt update && sudo apt install ffmpeg
pip install -U openai-whisper
pip install moviepy
"""
import whisper
from moviepy.editor import VideoFileClip
from whisper.utils import get_writer

# define file paths
video_file = "media/video.mp4"
audio_file = "media/audio.wav"
output_directory = "media/"


# Convert video to audio
clip = VideoFileClip(video_file)
audio = clip.audio
audio.write_audiofile(audio_file)

# Load audio and transcribe
model = whisper.load_model("base")
result = model.transcribe(audio_file)


# Save as a TXT file
txt_writer = get_writer("txt", output_directory)
txt_writer(result, audio_file)


# Save as an SRT file
srt_writer = get_writer("srt", output_directory)
srt_writer(result, audio_file)
