#!/usr/bin/env python3

import tkinter as tk 
import customtkinter as ctk



def combine_funcs(*funcs):
    def inner_combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return inner_combined_func

class Main(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Youtube Downloader")
        self.geometry("400x200")
        self.resizable(0,0)
        self.link_var = ctk.StringVar()
        self.title_label = ctk.CTkLabel(self,
                               text = "YouTube Video Downloader",
                               width = 120,
                               height = 25,
                               text_color = ("red"),
                               font = ("Roboto", 25, "bold"),
                               corner_radius = 8)

        self.yt_label = ctk.CTkLabel(self,
                               text = "Youtube Link:",
                               width = 120,
                               height = 25,
                               fg_color = ("red"),
                               font = ("Roboto", 15),
                               corner_radius = 8)
        self.ent = ctk.CTkEntry(self,
                               textvariable = self.link_var,  
                               width = 270,
                               height = 25,
                               border_width = 2,
                               corner_radius = 8)
        self.video_btn = ctk.CTkButton(self,
                                 width = 70,
                                 height = 42,
                                 border_width = 2,
                                 corner_radius = 8,
                                 text = "Video",
                                 command = "video")
        self.audio_btn = ctk.CTkButton(self,
                                 width = 70,
                                 height = 42,
                                 border_width = 2,
                                 corner_radius = 8,
                                 text = "Audio",
                                 command = "audio")
        self.video_title = ctk.CTkLabel(self,
                               text = '',
                               width = 80,
                               height = 22,
                               corner_radius = 8)
    def main_menu_place(self):
        self.title_label.place(relx = 0.5, rely = 0.1, anchor = tk.N)  #program title label
        self.yt_label.place(relx = 0.5, rely = 0.3, anchor = tk.N)  #entry title label
        self.ent.place(relx = 0.5, rely = 0.45, anchor = tk.N )  #entry bar
        self.video_btn.place(relx = 0.6, rely = 0.95, anchor = tk.S)   #video button
        self.audio_btn.place(relx = 0.4, rely = 0.95, anchor = tk.S)   #audio button

    def place_download_widgets(self):
        self.video_title.place(relx = 0.5, rely = 0.72, anchor = tk.S)


class window(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("300x100")
        self.title("Warning!")
        self.geometry("300x100")
        self.resizable(0,0)
        self.message_label = ctk.CTkLabel(self,
                               text = "Large File Warning!\nDo you wish to continue?",
                               width = 40,
                               height = 25,
                               corner_radius = 8)
        self.cancel_button = ctk.CTkButton(self,
                                 width = 40,
                                 height = 25,
                                 border_width = 2,
                                 corner_radius = 8,
                                 text = "Cancel",
                                 command = self.destroy)
        self.continue_button = ctk.CTkButton(self,
                                 width = 40,
                                 height = 25,
                                 border_width = 2,
                                 corner_radius = 8,
                                 text = "Continue",
                                 command = self.destroy)

    def place_widgets(self):
        self.message_label.place(relx = 0.5, rely = 0.3, anchor = tk.CENTER)
        self.cancel_button.place(relx = 0.3, rely =0.6, anchor = tk.N)
        self.continue_button.place(relx = 0.7, rely =0.6, anchor = tk.N)

