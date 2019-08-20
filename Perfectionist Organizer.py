#Импорт необходимых библиотек
import os
import re
import getpass
#Создание словарей с расширениями файлов и папкой, куда их нужно перекинуть
video_folder = {".3gp" : "Видео/", ".avi" : "Видео/", ".flv" : "Видео/", ".m4v" : "Видео/", ".mkv" : "Видео/", ".mov" : "Видео/", ".mp4" : "Видео/", ".wmv" : "Видео/", ".webm" : "Видео/"}
music_folder = {".mp3" : "Музыка/", ".aac": "Музыка/", ".flac" : "Музыка/", ".mpc" : "Музыка/", ".wma" : "Музыка/", ".wav" : "Музыка/"}
pic_folder = {".raw" : "Изображения/", ".jpg" : "Изображения/", ".tiff" : "Изображения/", ".psd" : "Изображения/", ".bmp" : "Изображения/", ".gif" : "Изображения/", ".png" : "Изображения/", ".jp2" : "Изображения/", ".jpeg" : "Изображения/"}
doc_folder = {".doc" : "Документы/", ".docx" : "Документы/", ".txt" : "Документы/", ".rtf" : "Документы/", ".pdf" : "Документы/", ".fb2" : "Документы/", ".djvu" : "Документы/", ".xls" : "Документы/", ".xlsx" : "Документы/", ".ppt" : "Документы/", ".pptx" : "Документы/", ".mdb" : "Документы/", ".accdb" : "Документы/", ".rar" : "Документы/", ".zip" : "Документы/", ".7z" : "Документы/"}
#Справшиваем у юзверя, как называется папка с загрузками (по-умолчанию: Загрузки)
user_downloads_path = input("Как у вас называется папка с загрузками? (по-умолчанию: Загрузки) ") or "Загрузки"
#Определяем имя пользователя в системе
usermane = getpass.getuser()
#Задаём путь к папке с загрузками для конкретного пользователя
downloads_path = os.listdir("/home/" + usermane + "/" + user_downloads_path)
#Путь до папки загрузок
default_path_d = "/home/" + usermane + "/" + user_downloads_path + "/"
# Путь вида /home/имяпользователя
default_path_u = "/home/" + usermane + "/"
#Проверяем есть ли в папке загрузок видеофайлы. Если есть, кидаем их в папку Видео
for video_format in video_folder:
    for name_file in downloads_path:
        if name_file.endswith(video_format):
            result = name_file.split(str(video_format), 1)
            os.rename(default_path_d + result[0] + video_format, default_path_u + video_folder.get(video_format) + result[0] + video_format)
#Проверяем есть ли в папке загрузок аудиофайлы. Если есть, кидаем их в папку Музыка
for music_format in music_folder:
    for name_file in downloads_path:
        if name_file.endswith(music_format):
            result = name_file.split(str(music_format), 1)
            os.rename(default_path_d + result[0] + music_format, default_path_u + music_folder.get(music_format) + result[0] + music_format)
#Проверяем есть ли в папке загрузок изображения. Если есть, кидаем их в папку Изображения
for pic_format in pic_folder:
    for name_file in downloads_path:
        if name_file.endswith(pic_format):
            result = name_file.split(str(pic_format), 1)
            os.rename(default_path_d + result[0] + pic_format, default_path_u + pic_folder.get(pic_format) + result[0] + pic_format)
#Проверяем есть ли в папке загрузок документы или архивы. Если есть, кидаем их в папку Документы
for doc_format in doc_folder:
    for name_file in downloads_path:
        if name_file.endswith(doc_format):
            result = name_file.split(str(doc_format), 1)
            os.rename(default_path_d + result[0] + doc_format, default_path_u + doc_folder.get(doc_format) + result[0] + doc_format)