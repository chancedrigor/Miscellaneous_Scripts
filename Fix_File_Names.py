# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 17:46:54 2016

@author: Cheng
"""

import os

for filename in os.listdir():
    if str(filename).find(" ") != -1:
        newname = str(filename).replace(" ", "_")
        os.rename(filename, newname)
