import io
import glob
import os
from shutil import move
from os.path import join
from os import listdir, rmdir

target_folder = 'dataset/tiny-imagenet-200/val'
test_folder   = 'dataset/tiny-imagenet-200/test'

os.mkdir(test_folder)
val_dict = {}
with open('dataset/tiny-imagenet-200/val/val_annotations.txt', 'r') as f:
    for line in f.readlines():
        split_line = line.split('\t')
        val_dict[split_line[0]] = split_line[1]
        
paths = glob.glob('dataset/tiny-imagenet-200/val/images/*')
for path in paths:
    file = path.split('/')[-1]
    folder = val_dict[file]
    if not os.path.exists(target_folder + '/' + str(folder)):
        os.mkdir(target_folder + '/' + str(folder))
        os.mkdir(target_folder + '/' + str(folder) + '/images')
    if not os.path.exists(test_folder + '/' + str(folder)):
        os.mkdir(test_folder + '/' + str(folder))
        os.mkdir(test_folder + '/' + str(folder) + '/images')
        
        
for path in paths:
    file = path.split('/')[-1]
    folder = val_dict[file]
    if len(glob.glob(target_folder + '/' + str(folder) + '/images/*')) <25:
        dest = target_folder + '/' + str(folder) + '/images/' + str(file)
    else:
        dest = test_folder + '/' + str(folder) + '/images/' + str(file)
    move(path, dest)
    
rmdir('dataset/tiny-imagenet-200/val/images')
