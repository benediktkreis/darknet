#!/usr/bin/env python3

import os, glob, fnmatch, shutil

#paths
read_img = "./data/ts/"
read_annotated_label = read_img
read_val_label = "./data/val.txt"
write_img = "./test/test_images/"
write_label = "./test/annotated_labels_test_images/"

#read val.txt to get labels that are to be used for testing
with open(read_val_label) as o:
    val_data_list = [line.rstrip() for line in o]

print("Convert data")
val_labels = []
for i in val_data_list:
    file_name = os.path.basename(i)
    val_labels.append(file_name)


#select all images
rgb = fnmatch.filter(os.listdir(read_img), '*.jpg')
annotated_labels = fnmatch.filter(os.listdir(read_annotated_label), '*.txt')

#compare list of imgs to list of annotated_labels
annotated_labels_no_end = []
for i in annotated_labels:
    annotated_labels_no_end.append(i[:-4])

val_labels_no_end = []
for i in val_labels:
    val_labels_no_end.append(i[:-4])

img_no_end = []
for i in rgb:
    img_no_end.append(i[:-4])

#same elements
def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

#intersection zw rgb and annotated_labels
same_elems=intersection(img_no_end, val_labels_no_end)

print("Number of same elements = ", len(same_elems))


#copy corresponding images into a new training folder "data_final"
for i in same_elems:
    path = read_img+i+".jpg"
    shutil.copy(path, write_img)


#copy corresponding annotated_labels into a new training folder "data_final"
for i in same_elems:
    path = read_annotated_label+i+".txt"
    shutil.copy(path, write_label)

print("Done")