#!/usr/bin/env python3

from pytube import YouTube
import tkinter as tk 
from winreg import *
import shutil
import YTDWGUI
import YTDWlog


#fix if title has dot at the end for audio


main = YTDWGUI.Main()    #pull GUI from module and create a class instance
main.main_menu_place()

with OpenKey(HKEY_CURRENT_USER, 'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders') as key:     #find user download path 
    Downloads = QueryValueEx(key, '{374DE290-123F-4565-9164-39C4925E467B}')[0]

def execute_video():     #intermediate function to push to actual download 
    yt = YouTube(formated_link())  #define pytube instance
    main.video_title.configure(text = yt.title)      #show details of URL in GUI
    main.place_download_widgets()
    yd = yt.streams.get_highest_resolution()
    if yd.filesize_gb > 5:
        warn_window = YTDWGUI.window()   #create warning if file is very big
        warn_window.continue_button.configure(command = lambda:execute_video_download())
        warn_window.place_widgets()

        YTDWlog.size_warning_logger(yt.title, "mp4", yd.filesize_gb)   #log warning 
    else:
        execute_video_download()
        print(yd.default_filename)

def execute_video_download():
    yt = YouTube(formated_link())  #define pytube instance
    main.video_title.configure(text = yt.title)
    main.place_download_widgets()
    yd = yt.streams.get_highest_resolution()
    yd.download(Downloads)  

    YTDWlog.info_logger(yt.title, "mp4", yd.filesize_gb)   #log downloa 

def execute_audio():
    yt = YouTube(formated_link())
    main.video_title.configure(text = yt.title)
    main.place_download_widgets()
    yd = yt.streams.filter(only_audio= True).all() #get only audio for all instances
    
    if yd[0].filesize_gb > 5:
        warn_window = YTDWGUI.window()
        warn_window.continue_button.configure(command = lambda:execute_audio_download())
        warn_window.place_widgets()

        YTDWlog.size_warning_logger(yt.title, "mp3", yd[0].filesize_gb)
    else:
        execute_audio_download()

def execute_audio_download():
    yt = YouTube(formated_link())
    main.video_title.configure(text = yt.title)
    main.place_download_widgets()
    yd = yt.streams.filter(only_audio= True).all()  #get only audio for all instances
    yd[0].download(Downloads)
    shutil.move(Downloads + '\\' + yt.title +'.mp4', Downloads + '\\' + yt.title +'.mp3')  #rename file to convert to mp3 
    
    YTDWlog.info_logger(yt.title, "mp3", yd[0].filesize_gb)

def formated_link():
    return '"' + main.link_var.get() + '"'    #format link to work with pytube as it only works in quotes

main.video_btn.configure(command = lambda: execute_video())
main.audio_btn.configure(command = lambda: execute_audio())


if __name__ == "__main__":    #run GUI
    main.mainloop()
