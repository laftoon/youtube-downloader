#!/usr/bin/env python3

import logging
import logging.handlers
import os 

#add gui errors for invalid link and add to logger 
#add file exists already warning and add to logger
#add file exists option to continue or not and add to logger 

f = open("YTDWlog.txt", 'a', newline='')
os.path.abspath("YTDWlog.txt")

log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logger = logging.getLogger(__name__)
logger.setLevel('DEBUG')
#handler = logging.FileHandler(r"C:\Users\laura\OneDrive\Desktop\Python scripts\YTDW\YTDWlog.txt")
handler = logging.FileHandler(os.path.abspath("YTDWlog.txt"))
formatter = logging.Formatter(log_format)
handler.setFormatter(formatter)
logger.addHandler(handler)
#logger.info("Downloaded \"{}\" in {} format, size: {} GB".format("blabla", "blaba", "blabla"))

def info_logger(title, dformat, size):
    logger.info("Downloaded \"{}\" in {} format, size: {} GB".format(title, dformat, size))

def size_warning_logger(title, dformat, size):
    logger.warning("File \"{}\".{} exceeds 5GB, size: {} GB, size warning: Very large file".format(title, dformat, size))

def invalid_link_error(title, dformat, size):
    pass

def file_exists_warning(title, dformat, size):
    pass

f.close()