'''
newpost.py
21 March 2017 22:19:29

Automates the creation of a new blog post.
'''
import os
from datetime import datetime, date, time

POSTTITLE = "blah"

POSTDIR = "_post"

CURRENTDIR = os.getcwd()

POSTPATH = CURRENTDIR + "\\" + POSTDIR + "\\" + POSTTITLE

CONTENT = '''
---
layout: post
title:  "{}"
excerpt: 
date:   {}
categories: post 
author: luke_griffith
---
'''

date = datetime.now()
time = date.time()

datestring = "{}-{}-{} {}:{}:{}".format(date.year, date.month, date.day, time.hour, time.minute, time.second)

Formatted = CONTENT.format(POSTTITLE, datestring)

open(POSTPATH)



