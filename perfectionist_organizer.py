#Импорт необходимых библиотек
import os
import getpass
import platform

# Создание словарей с расширениями файлов и папкой, куда их нужно перекинуть
video_folder = {".3gp": "Видео/", ".avi": "Видео/", ".flv": "Видео/", ".m4v": "Видео/", ".mkv": "Видео/",
                ".mov": "Видео/", ".mp4": "Видео/", ".wmv": "Видео/", ".webm": "Видео/"}
music_folder = {".mp3": "Музыка/", ".aac": "Музыка/", ".flac": "Музыка/", ".mpc": "Музыка/", ".wma": "Музыка/",
                ".wav": "Музыка/"}
pic_folder = {".raw": "Изображения/", ".jpg": "Изображения/", ".tiff": "Изображения/", ".psd": "Изображения/",
              ".bmp": "Изображения/", ".gif": "Изображения/", ".png": "Изображения/", ".jp2": "Изображения/",
              ".jpeg": "Изображения/"}
doc_folder = {".doc": "Документы/", ".docx": "Документы/", ".txt": "Документы/", ".rtf": "Документы/",
              ".pdf": "Документы/", ".fb2": "Документы/", ".djvu": "Документы/", ".xls": "Документы/",
              ".xlsx": "Документы/", ".ppt": "Документы/", ".pptx": "Документы/", ".mdb": "Документы/",
              ".accdb": "Документы/", ".rar": "Документы/", ".zip": "Документы/", ".7z": "Документы/"}


def main():
    #Проверка операционной системы, которой пользуется юзер
    type_os = platform.system()
    #Справшиваем у юзверя, как называется папка с загрузками (по-умолчанию: Загрузки)
    if type_os == "Linux":
        user_downloads_path = input("Как у вас называется папка с загрузками? (по-умолчанию: Загрузки) ") or "Загрузки"
    if type_os == "Windows":
        user_downloads_path = input("Как у вас называется папка с загрузками? (по-умолчанию: Загрузки) ") or "Downloads"
    #Определяем имя пользователя в системе
    usermane = getpass.getuser()
    #Путь до папки с загрузками
    if type_os == "Linux":
        default_path_d = "/home/" + usermane + "/" + user_downloads_path + "/"
    else:
        default_path_d_win = r"C:/Users/" + usermane + r"/" + user_downloads_path+ r"/"
    #Задаём путь к папке с загрузками для конкретного пользователя
    if type_os == "Linux":
        downloads_path = os.listdir("/home/" + usermane + "/" + user_downloads_path)
    else:
        downloads_path_win = os.listdir(r"C:/Users/" + usermane + r"/" + user_downloads_path)
    # Путь вида /домашняяпапка/имяпользователя
    if type_os == "Linux":
        default_path_u = "/home/" + usermane + "/"
    else:
        default_path_u_win = r"C:/Users/" + usermane + r"/"
    #Проверяем есть ли в папке загрузок видеофайлы. Если есть, кидаем их в папку Видео
    for video_format in video_folder:
        if type_os == "Linux":
            for name_file in downloads_path:
                if name_file.endswith(video_format):
                    result = name_file.split(str(video_format), 1)
                    os.rename(default_path_d + result[0] + video_format, default_path_u + video_folder.get(video_format) + result[0] + video_format)
        if type_os == "Windows":
            for name_file in downloads_path_win:
                if name_file.endswith(video_format):
                    result = name_file.split(str(video_format), 1)
                    os.rename(default_path_d_win + result[0] + video_format, default_path_u_win + "Videos" + r"/" + result[0] + video_format)
    #Проверяем есть ли в папке загрузок аудиофайлы. Если есть, кидаем их в папку Музыка
    for music_format in music_folder:
        if type_os == "Linux":
            for name_file in downloads_path:
                if name_file.endswith(music_format):
                    result = name_file.split(str(music_format), 1)
                    os.rename(default_path_d + result[0] + music_format, default_path_u + music_folder.get(music_format) + result[0] + music_format)
        if type_os == "Windows":
            for name_file in downloads_path_win:
                if name_file.endswith(music_format):
                    result = name_file.split(str(music_format), 1)
                    os.rename(default_path_d_win + result[0] + music_format, default_path_u_win + "Music" + r"/" + result[0] + music_format)
    #Проверяем есть ли в папке загрузок изображения. Если есть, кидаем их в папку Изображения
    for pic_format in pic_folder:
        if type_os == "Linux":
            for name_file in downloads_path:
                if name_file.endswith(pic_format):
                    result = name_file.split(str(pic_format), 1)
                    os.rename(default_path_d + result[0] + pic_format, default_path_u + pic_folder.get(pic_format) + result[0] + pic_format)
        if type_os == "Windows":
            for name_file in downloads_path_win:
                if name_file.endswith(pic_format):
                    result = name_file.split(str(pic_format), 1)
                    os.rename(default_path_d_win + result[0] + pic_format, default_path_u_win + "Pictures" + r"/" + result[0] + pic_format)
    #Проверяем есть ли в папке загрузок документы или архивы. Если есть, кидаем их в папку Документы
    for doc_format in doc_folder:
        if type_os == "Linux":
            for name_file in downloads_path:
                if name_file.endswith(doc_format):
                    result = name_file.split(str(doc_format), 1)
                    os.rename(default_path_d + result[0] + doc_format, default_path_u + doc_folder.get(doc_format) + result[0] + doc_format)
        if type_os == "Windows":
            for name_file in downloads_path_win:
                if name_file.endswith(doc_format):
                    result = name_file.split(str(doc_format), 1)
                    os.rename(default_path_d_win + result[0] + doc_format, default_path_u_win + "Documents" + r"/" + result[0] + doc_format)
    #Запрос на удаление оставшихся файлов в директории загрузок
    delete_user_confirm = input('Удалить из папки загрузок оставшиеся файлы? Напишите да или нет (по-умолчанию: нет) ' or 'нет')
    if delete_user_confirm == 'да':
        if type_os == "Linux":
            files_to_remove = os.listdir(default_path_d)
            for remove_files in files_to_remove:
                os.remove(default_path_d + "/" + remove_files)
        if type_os == "Windows":
            files_to_remove = os.listdir(default_path_d_win)
            for remove_files in files_to_remove:
                os.remove(default_path_d_win + "/" + remove_files)
    else:
        print('Программа завершила работу. Все файлы размещены.')


if __name__ == '__main__':
    main()
