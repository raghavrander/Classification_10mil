#!/usr/bin/env python
# coding: utf-8

# In[5]:


import csv

# Set the paths for your input text files and output CSV file
txt_file_path_1 = "CUB_200_2011/images.txt"
txt_file_path_2 = "CUB_200_2011/train_test_split.txt"
csv_file_path = "CUB_200_2011/images.csv"

# Read the data from the first text file
with open(txt_file_path_1, 'r') as txt_file_1:
    lines_1 = txt_file_1.readlines()

# Read the data from the second text file
with open(txt_file_path_2, 'r') as txt_file_2:
    lines_2 = txt_file_2.readlines()

# Convert the data from the first text file to CSV format and write to the CSV file
with open(csv_file_path, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')
    for line_1, line_2 in zip(lines_1, lines_2):
        data_1 = line_1.strip().split()
        data_2 = line_2.strip().split()
        csv_writer.writerow(data_1 + data_2)


# In[6]:


import os

# Set the path to your images directory and create train and test directories
images_folder = "C:/Users/Admin/Desktop/gnr638/dataset/CUB_200_2011/images"

# Create train and test directories if they don't exist
train_folder = "C:/Users/Admin/Desktop/gnr638/dataset/CUB_200_2011/train"
test_folder = "C:/Users/Admin/Desktop/gnr638/dataset/CUB_200_2011/test"
os.makedirs(train_folder, exist_ok=True)
os.makedirs(test_folder, exist_ok=True)

# Fetch the names of all folders in the images directory
folders = [folder for folder in os.listdir(images_folder) if os.path.isdir(os.path.join(images_folder, folder))]

# Create empty folders in train and test directories based on the folder names
for folder in folders:
    train_category_folder = os.path.join(train_folder, folder)
    test_category_folder = os.path.join(test_folder, folder)

    os.makedirs(train_category_folder, exist_ok=True)
    os.makedirs(test_category_folder, exist_ok=True)


# In[7]:


import os
import shutil
with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for _, image_path, _, split_value in csv_reader:
        category = image_path.split('/')[0]

        source_path = os.path.join("CUB_200_2011/images", image_path)  # Adjust this path if needed

        if int(split_value) == 1:
            destination_folder = os.path.join(train_folder, category)
        else:
            destination_folder = os.path.join(test_folder, category)

        destination_path = os.path.join(destination_folder, os.path.basename(image_path))
        shutil.copy(source_path, destination_path)


# In[ ]:




