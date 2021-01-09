import os
import shutil

'''
This script organizes images taken from red and green channels
and puts them in separate red and green folders. 

The three main steps are:
1. open each tifs folder sequentially
2. within each tifs folder, open .tif_files sequentially
3. within each .tifs_files folder:
    a. make red folder
    b. make green folder
    c. obtain .tif filenames
        i. if .tif filename contains c1x0, move to red folder
        ii. if .tif filename contains c0x0, move to green folder
        iii. copy/paste BF files to red and green folders
'''

# STEP 1

# get all folders
all_folders = os.listdir(os.getcwd())

# get only tifs folders
tifs_folders = []

for folder in all_folders:
    if 'tifs' in folder:
        tifs_folders.append(folder)

# organize tifs folders
tifs_folders_sorted = sorted(tifs_folders)

# change directory to tifs_folders and open each tifs folder
for each_folder in tifs_folders_sorted:
    folder_path = "/" + each_folder
    abs_folder_path = "/file/path/goes/here" + folder_path
    folder_directory = os.chdir(abs_folder_path)

    # STEP 2

    # open tif files in each tifs folder; first, get all files
    all_files = os.listdir(os.getcwd())

    # extract only tif files and BF files
    tif_files = []
    BF_tif_files = []

    for file in all_files:
        if '.tif_files' in file:
            tif_files.append(file)
        else:
            if 'BF' in file:
                BF_tif_files.append(file)

    # organize tif files and BF files
    tif_files_sorted = sorted(tif_files)
    BF_tif_files_sorted = sorted(BF_tif_files)

    # move BF tif files into tif_files folder
    for i in range(len(tif_files_sorted)):
        shutil.move(BF_tif_files_sorted[i], tif_files_sorted[i])

    # STEP 3

    # open each tif files folder
    for each_tif_files in tif_files_sorted:
        tif_file_path = "/" + each_tif_files
        abs_tif_file_path = abs_folder_path + tif_file_path
        tif_file_directory = os.chdir(abs_tif_file_path)

        # make red folder
        absolute_red_path = abs_tif_file_path + "/red"
        os.mkdir(absolute_red_path)

        # make green folder
        absolute_green_path = abs_tif_file_path + "/green"
        os.mkdir(absolute_green_path)

        # get all files within tif_files folder
        all_tif_files = os.listdir(os.getcwd())

        for tif_file_data in all_tif_files:
            # get out the red channel data
            # and move to red channel folder
            if 'c1x0' in tif_file_data:
                if 'metadata' in tif_file_data:
                    pass
                else:
                    shutil.move(tif_file_data, 'red')
            # get out the red channel data
            # and move to green channel folder
            elif 'c0x0' in tif_file_data:
                if 'metadata' in tif_file_data:
                    pass
                else:
                    shutil.move(tif_file_data, 'green')
            # copy/paste the BF file into red and green folders
            else:
                if 'BF' in tif_file_data:
                    shutil.copy(tif_file_data, 'red')
                    shutil.copy(tif_file_data, 'green')

print('Data are now organized into red and green folders.')
