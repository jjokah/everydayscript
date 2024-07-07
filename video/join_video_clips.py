from moviepy.editor import VideoFileClip, concatenate_videoclips

def join_videos(video1_path, video2_path, output_path):
    # Load the video clips
    clip1 = VideoFileClip(video1_path)
    clip2 = VideoFileClip(video2_path)
    
    # Concatenate the clips
    final_clip = concatenate_videoclips([clip1, clip2])
    
    # Write the result to a file
    final_clip.write_videofile(output_path)
    
    # Close the clips to free up system resources
    clip1.close()
    clip2.close()
    final_clip.close()

# Example usage
join_videos("clip1.mp4", "clip2.mp4", "merged_video.mp4")
