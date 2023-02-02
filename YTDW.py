#!/usr/bin/env python3

#imports

from pytube import YouTube
import tkinter as tk 
import customtkinter as ctk
from winreg import *

#define parent window
#and make input a string 

root = ctk.CTk()
root.title("Youtube Downloader")
root.geometry("400x200")
link_var = ctk.StringVar()

#find univ downloads path

with OpenKey(HKEY_CURRENT_USER, 'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders') as key:
    Downloads = QueryValueEx(key, '{374DE290-123F-4565-9164-39C4925E467B}')[0]

#define video download function for button

def execute():
    link_unformated = link_var.get()  #get unformated link without quotes
    link_formated = '"' + link_unformated + '"'   #add quotes
    yt = YouTube(link_formated)  #define pytube instance

    video_title = ctk.CTkLabel(master = root,
                               text = yt.title,
                               width = 120,
                               height = 25,
                               corner_radius = 8)
    video_title.place(relx = 0.5, rely = 0.75, anchor = tk.S) #show label with video title for confirmation


    yd = yt.streams.get_highest_resolution()
    yd.download(Downloads)  #download yt video at highest resolution



#make gui

ct_coordx = 0.5 #center coordinate for ctkinter instances
title_label = ctk.CTkLabel(master = root,
                               text = "YouTube Video Downloader",
                               width = 120,
                               height = 25,
                               text_color = ("red"),
                               font = ("Roboto", 25, "bold"),
                               corner_radius = 8)
title_label.place(relx = ct_coordx, rely = 0, anchor = tk.N)  #program title label

yt_label = ctk.CTkLabel(master = root,
                               text = "Youtube Link:",
                               width = 120,
                               height = 25,
                               fg_color = ("red"),
                               font = ("Roboto", 15),
                               corner_radius = 8)
yt_label.place(relx = ct_coordx, rely = 0.3, anchor = tk.N)  #entry title label

ent = ctk.CTkEntry(master = root,
                               textvariable = link_var,  
                               width = 270,
                               height = 25,
                               border_width = 2,
                               corner_radius = 8)
ent.place(relx = ct_coordx, rely = 0.45, anchor = tk.N )  #entry bar

apply_btn = ctk.CTkButton(master=root,
                                 width = 60,
                                 height = 42,
                                 border_width = 2,
                                 corner_radius = 8,
                                 text = "Apply",
                                 command = execute)
apply_btn.place(relx = 0.5, rely = 1, anchor = tk.S)   #enter button

root.mainloop()