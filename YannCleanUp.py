from pathlib import Path
import os, time, shutil
from stat import S_ISREG, ST_CTIME, ST_MODE


class fileToMove():
    def __init__(self, name, folder, date):
        self.name = name
        self.folder = folder
        self.date = date

info_list = []
info_dict = {}
file_type_dict = dict(CR2 = 'CR2', CR3 = 'CR3', dng = 'DNG', jpg = 'JPG', jpeg = 'JPG', JPG = 'JPG', bmp = 'IMAGES',
                      png = 'IMAGES', ico = 'IMAGES', mp4 = 'Video', MP4 = 'Video', avi = 'Video', mov = 'Video')
destination_path = Path("F:/Yannis/SortingDestination/")
origin_path = Path('F:/Yannis/Photos/2019/9-2-2019/')

for dirname, dirnames, filenames in os.walk(origin_path):
    for subdirname in dirnames:
        dirpath = os.path.join(dirname, subdirname)
        data = (os.path.join(dirpath, fn) for fn in os.listdir(dirpath))
        data = ((os.stat(path), path) for path in data)
        data = ((stat[ST_CTIME], path) for stat, path in data if S_ISREG(stat[ST_MODE]))
        for cdate, path in sorted(data):
            fl = fileToMove(os.path.basename(path), path, time.ctime(cdate))
            info_list.append(fl)
            print(fl.date)
for filez in info_list:
    file_date = str(filez.date).split()
    file_name = str(filez.name).split('.')
    file_folder = str(filez.folder)
    if file_name[1] not in file_type_dict:
        destination_folder3 = destination_path / 'Uncategorized'
        FROM = file_folder
        TO = destination_folder3 / filez.name
        shutil.move(FROM, TO)
    else:
        for key, value in file_type_dict.items():
            if key == file_name[1]:
                year_exists = False
                month_exists = False
                day_exists = False
                destination_folder = destination_path / value
                for folder_year in os.listdir(destination_folder):
                    if folder_year == file_date[4]:
                        destination_folder_year = destination_folder / folder_year
                        year_exists = True
                        for folder_month in os.listdir(destination_folder_year):
                            if folder_month == file_date[1]:
                                destination_folder_month = destination_folder_year / folder_month
                                month_exists = True
                                for folder_day in os.listdir(destination_folder_month):
                                    if folder_day == file_date[2]:
                                        day_exists = True
                                        FROM = file_folder
                                        TO = destination_folder_year / folder_month / folder_day / filez.name
                                        shutil.move(FROM, TO)
                if not year_exists:
                    os.mkdir(destination_path / value / file_date[4])
                if not month_exists:
                    os.mkdir(destination_path / value / file_date[4] / file_date[1])
                if not day_exists:
                    os.mkdir(destination_path / value / file_date[4] / file_date[1] / file_date[2])
                    destination_folder2 = destination_path / value / file_date[4] / file_date[1] /file_date[2]
                    FROM = file_folder
                    TO = destination_folder2 / filez.name
                    shutil.move(FROM, TO)
