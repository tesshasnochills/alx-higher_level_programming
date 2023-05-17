#!/usr/bin/python3
 
def uniq_add(my_list=[]):
    new_set = set(my_list)
    uniq = 0
    for x in new_set:
        uniq += x
    return uniq
