# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 08:48:58 2022

@author: alessandra.gherardel
"""

lst = [(255, 255, 255), 0, 0, (255, 255, 255), (255, 255, 255), 0, (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), (255, 255, 255), 0, (255, 255, 255)]
        
def longest_streak(lst, item_to_find):
    count = 0
    result = []
    for i, item in enumerate(lst):
        try:
            if lst[i] == item_to_find:
                count += 1
            if lst[i + 1] != item_to_find:
                result.append(count)
                count = 0
        except IndexError:
            result.append(count)
            count = 0
    return result

