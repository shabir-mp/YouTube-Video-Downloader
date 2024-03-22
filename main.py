from pytube import YouTube
import os, time


def home():
   print("\033[31mYoutube Video Downloader\033[0m")
   print("1. Download Video \n2. See Download History")
   inpt = input("> ").strip().lower()
   if inpt == "1":
      download()
   elif inpt == "2":
      history()
   else:
      print("Input not valid. You will directed to download.")
      time.sleep(2)
      os.system("clear")
      download()


def download():
   os.system("clear")
   try:
      url = input("Enter the YouTube Video URL: ")
      yt = YouTube(url)
      os.system("clear")
      print("Video URL  :", url)
      print("Video Title:", yt.title)
      print("Video Views:", yt.views)
      print()
      print("\033[32mVideo caught. Request the highest resolution...\033[0m")
      yd = yt.streams.get_highest_resolution()
      os.system("clear")
      print("Video URL  :", url)
      print("Video Title:", yt.title)
      print("Video Views:", yt.views)
      print()
      print(
          "\033[32mThe highest resolution video has been obtained. Downloading Videos...\033[0m"
      )
      yd.download()
      os.system("clear")
      print("\033[32mDownload complete.\033[0m")
      f = open("history.yt", "a+")
      f.write(
          f"\nVideo URL: {url}\nVideo Title: {yt.title}\nVideo Views: {yt.views}"
      )
      f.write("\n-----------------")
      f.close()
      time.sleep(2)
      os.system("clear")
      home()
   except Exception as e:
      print("An error occurred:", str(e))
      time.sleep(2)
      os.system("clear")
      home()


def history():
   os.system("clear")
   f = open("history.yt", "r")
   data = f.read()
   print(data)
   print()
   exit = input("Press enter to exit. ")
   os.system("clear")
   home()


home()
