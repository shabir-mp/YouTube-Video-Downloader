import tkinter as tk
from tkinter import ttk, messagebox
from pytube import YouTube

def download():
    accepted = acceptvar.get()
    if accepted == "Accepted":
        link = linkinpt.get()
        resolution = resinpt.get()

        try:
            youtube_video = YouTube(link)
            video_stream = youtube_video.streams.filter(resolution="{}p".format(resolution)).first()
            if video_stream is not None:
                video_stream.download()
                status.set("Video downloaded successfully!")
            else:
                status.set("No video stream found with the specified resolution. Please try another resolution.")
                tk.messagebox.showwarning(title="Resolution Error", message="No video stream found with the specified resolution. Please try another resolution.")
        except Exception as e:
            errmsg = "Error: ", e
            status.set(errmsg)
            tk.messagebox.showwarning(title="Something Went Wrong", message="Can't find video. Please check again the video link. Check the status for detail.")
    else:
        status.set("Terms and Condition Error")
        tk.messagebox.showwarning(title="Terms and Condition Check", message="Please Agree the Terms and Conditions to Download Video")

def vidinfo():
    accepted = acceptvar.get()
    if accepted == "Accepted":
            linkget = linkinpt.get()
            youtube_video = YouTube(linkget)
            titleshow = youtube_video.title
            viewshow = youtube_video.views
            ratingshow = youtube_video.rating
            authorshow = youtube_video.author
            pubshow = youtube_video.publish_date
            lengthshow = youtube_video.length
            thumbshow = youtube_video.thumbnail_url
            title.set(titleshow)
            viewers.set(viewshow)
            rating.set(ratingshow)
            author.set(authorshow)
            pub.set(pubshow)
            length.set(lengthshow)
            thumb.set(thumbshow)
    else:
        status.set("Terms and Condition Error")
        tk.messagebox.showwarning(title="Terms and Condition Check", message="Please Agree the Terms and Conditions to Download Video")

root = tk.Tk()
root.title("Youtube Video Downloader")

frame = ttk.Frame(root)
frame.grid(row=0, column=0)

#Link
linkframe = ttk.LabelFrame(frame, text="Download Option")
linkframe.grid(row=0, column=0)

link = ttk.Label(linkframe, text="Video Link")
link.grid(row=0, column=0, padx=5, pady=10)
linkinpt = ttk.Entry(linkframe)
linkinpt.grid(row=0, column=1, padx=5, pady=10)

resolution = ttk.Label(linkframe, text="Video Resolution")
resinpt = ttk.Combobox(linkframe, value=["2160","1440","1080","720","480","360","240","144"])
resolution.grid(row="1", column="0", padx=5, pady=10)
resinpt.grid(row="1", column="1", padx=5, pady=10)

#Download and Check
downloadlabel = ttk.LabelFrame(frame, text="Download and Information")
downloadlabel.grid(row="1",column="0")
acceptvar = tk.StringVar(value="Not Accepted")
terms_check = ttk.Checkbutton(downloadlabel, text="I accept the terms and conditions.", variable=acceptvar, onvalue="Accepted", offvalue="Not Accepted")
terms_check.grid(row=0,column=0,padx=35)

downloadbtn = ttk.Button(downloadlabel, text="Download Video", command=download)
downloadbtn.grid(row=1,column=0,padx=10, pady=10, sticky="we")

infobtn = ttk.Button(downloadlabel, text="Get Video Information", command=vidinfo)
infobtn.grid(row=2,column=0,padx=10, pady=10, sticky="we")

for widget in frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

infolabel = ttk.LabelFrame(frame, text="Video Information")
infolabel.grid(row=0, column=1, padx=10, pady=5, rowspan=2)

title = tk.StringVar()
titletext = ttk.Label(infolabel, text="Title : ")
titlelabel = ttk.Label(infolabel, textvariable=title)
titlelabel.grid(row=0,column=1, padx=5, pady=5, sticky="w")
titletext.grid(row=0,column=0, padx=5, pady=5, sticky="e")

author = tk.StringVar()
authortext = ttk.Label(infolabel, text="Author : ")
authorlabel = ttk.Label(infolabel, textvariable=author)
authorlabel.grid(row=1,column=1, padx=5, pady=5, sticky="w")
authortext.grid(row=1,column=0, padx=5, pady=5, sticky="e")

viewers = tk.StringVar()
viewtext = ttk.Label(infolabel, text="Views : ")
viewlabel = ttk.Label(infolabel, textvariable=viewers)
viewlabel.grid(row=2,column=1, padx=5, pady=5, sticky="w")
viewtext.grid(row=2,column=0, padx=5, pady=5, sticky="e")

rating = tk.StringVar()
ratingtext = ttk.Label(infolabel, text="Rating : ")
ratinglabel = ttk.Label(infolabel, textvariable=rating)
ratinglabel.grid(row=3,column=1, padx=5, pady=5, sticky="w")
ratingtext.grid(row=3,column=0, padx=5, pady=5, sticky="e")

pub = tk.StringVar()
pubtext = ttk.Label(infolabel, text="Publish Date : ")
publabel = ttk.Label(infolabel, textvariable=pub)
publabel.grid(row=4,column=1, padx=5, pady=5, sticky="w")
pubtext.grid(row=4,column=0, padx=5, pady=5, sticky="e")

length = tk.StringVar()
lengthtext = ttk.Label(infolabel, text="Video Length (s) : ")
lengthlabel = ttk.Label(infolabel, textvariable=length)
lengthlabel.grid(row=5,column=1, padx=5, pady=5, sticky="w")
lengthtext.grid(row=5,column=0, padx=5, pady=5, sticky="e")

thumb = tk.StringVar()
thumbtext = ttk.Label(infolabel, text="Thumb URL : ")
thumblabel = ttk.Label(infolabel, textvariable=thumb)
thumblabel.grid(row=6,column=1, padx=5, pady=5, sticky="w")
thumbtext.grid(row=6,column=0, padx=5, pady=5, sticky="e")

title.set("Unknown")
viewers.set("Unknown")
rating.set("Unknown")
author.set("Unknown")
pub.set("Unknown")
length.set("Unknown")
thumb.set("Unknown")

statuslabel = ttk.LabelFrame(frame, text="Status")
statuslabel.grid(row=2, column=0, padx=10, pady=5, columnspan=2)
status = tk.StringVar()
statustext = ttk.Label(statuslabel, textvariable=status)
statustext.grid(row=0,column=0, padx=10, pady=5)
status.set("Download Video to See Status")

root.mainloop()
