#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    new_list = []
    if idx < 0 or idx > (len(my_list)) - 1:
        return my_list
    for x in range(len(my_list)):
        if x != idx:
            new_list.append(my_list[x])
        else:
            new_list.append(element)
    return new_list
