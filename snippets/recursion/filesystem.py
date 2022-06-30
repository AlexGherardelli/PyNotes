# -*- coding: utf-8 -*-
"""
Template for filesystem search
"""

import os


folder = os.getcwd()


def explore(folder, ext, lst=[]):
    """Returns all files of a certain extension contained in a folder."""\

    # for each item in a folder
    for item in os.listdir(folder):
        # concatenate 
        fullpath = folder + "/" + item
        if os.path.isfile(fullpath) and fullpath.endswith(ext):
            lst.append(item)
        elif os.path.isdir(fullpath):
            explore(fullpath, ext, lst)
    return lst


search_python = explore(folder, ".py", lst=[])
print(search_python)
