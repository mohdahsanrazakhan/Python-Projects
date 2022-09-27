from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

print(argv)
print(f"Title: {yt.title}")
print(f"Vies: {yt.views}")

yd = yt.streams.get_highest_resolution()

yd.download('path-directory')
