#!/usr/bin/python
def remove_duplicates(my_list):
    new_list = []
    for item in my_list:
    	if item not in new_list:
    		new_list.append(item)
    return new_list

print remove_duplicates([2, 3, 1, 2, 4, 1])