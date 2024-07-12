import os
import shutil

source_dir = 'C:/Users/dilji/Downloads'
destination_dir = 'D:/automanaged_files'

file_types = {
    'documents': ['.pdf', '.docx', '.txt'],
    'images': ['.jpg', '.jpeg', '.png', '.gif'],
    'videos': ['.mp4', '.avi'],
    'audio': ['.mp3', '.wav'],
    'archives': ['.zip', '.tar', '.gz'],
    'sql': ['.sql'],
    'svg': ['.svg'],
    'apk': ['.apk'],
    'excel': ['.xls', '.xlsx', '.csv'],
}

for folder in file_types.keys():
    folder_path = os.path.join(destination_dir, folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

for filename in os.listdir(source_dir):
    file_path = os.path.join(source_dir, filename)
    if os.path.isfile(file_path):
        for folder, extension in file_types.items():
            if filename.lower().endswith(tuple(extension)):
                shutil.move(file_path, os.path.join(destination_dir, folder, filename))
                break
