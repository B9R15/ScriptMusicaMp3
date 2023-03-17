import os 
from pytube import Playlist, YouTube
from moviepy.editor import*

playlist_url = "https://www.youtube.com/playlist?list=PLhyGPBpqYv4GzEX5VG1d3jheZINjwmshG"

playlist = Playlist(playlist_url)

for video_url in playlist.video_urls:

    video= YouTube(video_url)

    video_stream = video.streams.get_highest_resolution()
    video_file = video_stream.download()

    audio_file = os.path.splitext(video_file)[0] + ".mp3"
    video_clip = AudioFileClip(video_file)
    video_clip.write_audiofile(audio_file)
    os.remove(video_file)

    print("Descargada la canción:", video.title)


