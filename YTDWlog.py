#!/usr/bin/env python3

import logging
import logging.handlers
import os 

f = open("YTDWlog.txt", 'a', newline='')   #create logging file 
os.path.abspath("YTDWlog.txt")              #find absolute path of file as handler only works with absolute file 

log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logger = logging.getLogger(__name__)
logger.setLevel('DEBUG')
handler = logging.FileHandler(os.path.abspath("YTDWlog.txt"))
formatter = logging.Formatter(log_format)
handler.setFormatter(formatter)
logger.addHandler(handler)

def info_logger(title, dformat, size):
    logger.info("Downloaded \"{}\" in {} format, size: {} GB".format(title, dformat, size))

def size_warning_logger(title, dformat, size):
    logger.warning("File \"{}\".{} exceeds 5GB, size: {} GB, size warning: Very large file".format(title, dformat, size))

def invalid_link_error(title, dformat, size):
    pass

def file_exists_warning(title, dformat, size):
    pass

f.close()