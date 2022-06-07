# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 11:39:52 2022

@author: agher
"""

import os


folder = os.getcwd()


def explore(folder, ext, lst=[]):
    """Returns all files of a certain extension contained in a folder."""
    for item in os.listdir(folder):
        fullpath = folder + "/" + item
        if os.path.isfile(fullpath) and fullpath.endswith(ext):
            lst.append(item)
        elif os.path.isdir(fullpath):
            explore(fullpath, ext, lst)
    return lst


search_python = explore(folder, ".py", lst=[])
print(search_python)
