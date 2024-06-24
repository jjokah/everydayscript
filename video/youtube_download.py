import yt_dlp

def download_youtube_video(url, download_path):
  # Downloads a YouTube video to the given download path.
  # url: The YouTube video URL to download.  
  # download_path: The path to download the video to.
  # Uses yt_dlp to download the best available video and audio streams 
  # and saves it to download_path with the video title and extension.
  ydl_opts = {
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',
    'outtmpl': f'{download_path}/%(title)s.%(ext)s',
  }
  
  with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

if __name__ == '__main__':
  url = 'https://www.youtube.com/watch?v=F4tvM4Vb3A0&list=PLfYUBJiXbdtSvpQjSnJJ_PmDQB_VyT5iU&index=2'
  download_path = '/home/jjokah/Videos'
  
  download_youtube_video(url, download_path)
