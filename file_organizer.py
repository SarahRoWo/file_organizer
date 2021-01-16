'''This script organizes microscope images taken from red and green
channels and puts them into separate red and green folders.

The three main steps are:
1. Open each tifs folder sequentially.
2. Within each tifs folder, open .tif_files sequentially.
3. Within each .tifs_files folder:
    a. Create a red folder.
    b. Create a green folder.
    c. Obtain .tif filenames:
        i. If .tif filename contains c1x0, move to red folder.
        ii. if .tif filename contains c0x0, move to green folder
        iii. Copy and paste brightfield (BF) files to red and green
        folders.
'''


import os
import shutil


# STEP 1
# Get all folders.
all_folders = os.listdir(os.getcwd())

# Get only tifs folders.
tifs_folders = []
for folder in all_folders:
    if 'tifs' in folder:
        tifs_folders.append(folder)

# Organize tifs folders.
tifs_folders_sorted = sorted(tifs_folders)

# Change directory to tifs_folders and open each tifs folder.
for each_folder in tifs_folders_sorted:
    folder_path = "/" + each_folder
    abs_folder_path = "/file/path/goes/here" + folder_path
    folder_directory = os.chdir(abs_folder_path)

    # STEP 2
    # Open tif files in each tifs folder; first, get all files.
    all_files = os.listdir(os.getcwd())

    # Extract only tif files and BF files.
    tif_files = []
    BF_tif_files = []

    for file in all_files:
        if '.tif_files' in file:
            tif_files.append(file)
        else:
            if 'BF' in file:
                BF_tif_files.append(file)

    # Organize tif files and BF files.
    tif_files_sorted = sorted(tif_files)
    BF_tif_files_sorted = sorted(BF_tif_files)

    # Move BF tif files into tif_files folder.
    for i in range(len(tif_files_sorted)):
        shutil.move(BF_tif_files_sorted[i], tif_files_sorted[i])

    # STEP 3
    # Open each tif files folder.
    for each_tif_files in tif_files_sorted:
        tif_file_path = "/" + each_tif_files
        abs_tif_file_path = abs_folder_path + tif_file_path
        tif_file_directory = os.chdir(abs_tif_file_path)

        # Create red folder.
        absolute_red_path = abs_tif_file_path + "/red"
        os.mkdir(absolute_red_path)

        # Create green folder.
        absolute_green_path = abs_tif_file_path + "/green"
        os.mkdir(absolute_green_path)

        # Get all files within the tif_files folder.
        all_tif_files = os.listdir(os.getcwd())

        for tif_file_data in all_tif_files:
            # Get out the red channel data
            # and move to red channel folder.
            if 'c1x0' in tif_file_data:
                if 'metadata' in tif_file_data:
                    pass
                else:
                    shutil.move(tif_file_data, 'red')
            # Get out the green channel data
            # and move to green channel folder.
            elif 'c0x0' in tif_file_data:
                if 'metadata' in tif_file_data:
                    pass
                else:
                    shutil.move(tif_file_data, 'green')
            # Copy and paste the BF file into red and green folders.
            else:
                if 'BF' in tif_file_data:
                    shutil.copy(tif_file_data, 'red')
                    shutil.copy(tif_file_data, 'green')

print('Data are now organized into red and green folders.')
