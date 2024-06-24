"""
TODO: Rewrite code to use just os and exifread library
"""

import os
from datetime import datetime
from PIL import Image  # Import for handling various image formats

def get_exif_date(image_path):
    try:
        # Attempt to extract date from EXIF data
        with Image.open(image_path) as img:
            exif_data = img.getexif()
            if exif_data:
                date_tag = 36867  # Assuming EXIF DateTime tag
                date_time_str = exif_data.get(date_tag)
                if date_time_str:
                    return datetime.strptime(date_time_str, "%Y:%m:%d %H:%M:%S")
    except (OSError, IOError):
        # Handle potential file access errors
        pass
    return None  # Return None if EXIF date not found

def rename_image(old_path, new_path):
    try:
        os.rename(old_path, new_path)
        print(f"Renamed: {old_path} -> {new_path}")
    except OSError as e:
        print(f"Error renaming {old_path}: {e}")

def process_directory(directory):
    counter = 1
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.lower().endswith((".jpg", ".jpeg", ".png", ".bmp", ".gif")):  # Check common image extensions
                image_path = os.path.join(root, filename)
                exif_date = get_exif_date(image_path)
                if exif_date:
                    new_basename = exif_date.strftime("%Y-%m-%d")
                    if counter > 1:
                        new_basename += f"_{counter:03d}"
                    new_extension = os.path.splitext(filename)[1]
                    new_path = os.path.join(root, f"{new_basename}{new_extension}")
                    rename_image(image_path, new_path)
                    counter += 1  # Increment counter for duplicate dates

if __name__ == "__main__":
    directory = "/home/jjokah/Repos/everyday-script/image"
    process_directory(directory)
    print("Finished renaming images.")
