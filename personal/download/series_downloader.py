"""
Downloads all episodes of House M.D.
by interating over each season and episode,
downloading the video files,
and saving them to the appropriate folders

Requirements:
pip install tqdm
"""
import requests
from tqdm import tqdm
import os

# Define the seasons to download
seasons = list(range(1, 9))

# URL template for the video files
url_template = "http://d1.o2tv.org/House%20MD/Season%20{}/House%20MD%20-%20S{}E{}%20(O2TvSeries.Com).mp4"

# Create a media folder
os.makedirs("media", exist_ok=True)

# Create a folder for each season
for season_number in seasons:
    season_folder = f"Season {season_number}"
    os.makedirs(os.path.join("media/House MD/", season_folder), exist_ok=True)

    # Download episodes for the current season
    for episode_number in range(1, 25):
        # Construct the URL for the current episode
        url = url_template.format(
            str(season_number).zfill(2),
            str(season_number).zfill(2),
            str(episode_number).zfill(2),
        )

        # Send a GET request to the URL and get the response
        response = requests.get(url, stream=True)

        # Get the total file size in bytes
        file_size = int(response.headers.get("Content-Length", 0))

        # Save the content to a file in the season folder
        filename = f"media/House MD/{season_folder}/House MD - S{str(season_number).zfill(2)}E{str(episode_number).zfill(2)}.mp4"
        with open(filename, "wb") as f:
            # Use tqdm to show the progress of the download
            with tqdm(
                total=file_size, unit="B", unit_scale=True, desc=filename
            ) as pbar:
                for data in response.iter_content(chunk_size=1024):
                    # Write data to file
                    f.write(data)
                    # Update progress bar
                    pbar.update(len(data))

        print(f"Downloaded {filename}")
