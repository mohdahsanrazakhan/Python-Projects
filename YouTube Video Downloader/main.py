from tkinter import *
from turtle import color
from pytube import YouTube
from sys import argv

# Shows processing your video with YT url-link
def download():
    print(f"Downloading...\n{url.get()}")
    root.destroy()


# Screen Section
root = Tk()
root.geometry("400x200")
root.maxsize(400, 200)
root.minsize(400, 200)
root.title("YouTube Video Downloader")
root.configure(background="#282828")


# Label Section
yt_label = Label(text="Enter Video URL link", font="comicsansms 15 bold", pady=5, fg="white", bg="#282828")
yt_label.pack(padx=0.5, pady=0.5, anchor=CENTER)


# Entry Section
url = StringVar()
url_entry = Entry(root, textvariable=url, width=30)
url_entry.pack(padx=0.5, pady=0.5, anchor=CENTER)


# Button Section
btn = Button(root, text="Download", bg="red", fg="white", font="comicsansms 10 bold", command=download)
btn.pack(padx=0.5, pady=0.5, anchor=CENTER)


root.mainloop()


# YTD Section
link = str(url.get())
YouTube(link).streams.first().download('D:\Project\YouTube Video Downloader')
yt = YouTube(link)
# if you want a low resolution then change '.get_lowest_resolution()'
print(f"Title: {yt.title}")
yt.streams.get_highest_resolution()
print("Video Downloaded!")
