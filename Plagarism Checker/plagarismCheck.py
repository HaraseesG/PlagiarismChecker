# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 12:08:09 2019

@author: haras
"""

def line_split(text_original, text_created, list_csv):    
    with open(text_original, 'r', encoding="ANSI") as fo:
        with open(text_created, 'r', encoding="ANSI") as fc:
            lines_original = fo.readlines()
            lines_created = fc.readlines()
            
            for x in range(0, len(lines_original)):
                for y in range(0, len(lines_created)):
                    if (word_split(lines_original[x], lines_created[y], text_original, text_created) != 0.0):
                        list_csv.append(word_split(lines_original[x], lines_created[y], text_original, text_created))
            
            return list_csv
                 
def word_split(lines_original, lines_created, text_original, text_created):
    data_array = []
    original_array = []
    
    line_original = lines_original.split(' ')
    line_created = lines_created.split(' ')
    
    for word in line_original:
        original_array.append(word)
    
    for word in line_created:
        data_array.append(word)
        
    return comparisons(original_array, data_array, text_original, text_created)
    
def comparisons(original_array, data_array, text_original, text_created):
    counter = 0

    if len(original_array) > len(data_array):        
        for i in range(0, len(data_array)):
            if data_array[i] == original_array[i]:
                counter += 1
                i += 1
            else:
                i += 1
                
            length_of_line = counter/len(original_array)
    else:
        for i in range(0, len(original_array)):
            if data_array[i] == original_array[i]:
                counter += 1
                i += 1
            else:
                i += 1
    
    length_of_line = counter / len(original_array)
    return length_of_line

def some_func(text_original, text_created):
    list_csv = []
    sum_count = 0
    line_split(text_original, text_created, list_csv)

    for i in range(0, len(list_csv)):
        sum_count += list_csv[i]
    
    if len(list_csv) != 0:        
        sum_count = sum_count / len(list_csv)
   
    
    return sum_count
