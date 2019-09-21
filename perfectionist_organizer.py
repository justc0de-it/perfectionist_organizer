#Импорт необходимых библиотек
import os
import getpass
import platform

# Создание словарей с расширениями файлов и папкой, куда их нужно перекинуть
video_formats = [".3gp", ".avi", ".flv", ".m4v", ".mkv", ".mov", ".mp4", ".wmv", ".webm"]
music_formats = [".mp3", ".aac", ".flac", ".mpc", ".wma", ".wav"]
pic_formats = [".raw", ".jpg", ".tiff", ".psd", ".bmp", ".gif", ".png", ".jp2", ".jpeg"]
doc_formats = [".doc", ".docx", ".txt", ".rtf", ".pdf", ".fb2", ".djvu", ".xls",
               ".xlsx", ".ppt", ".pptx", ".mdb", ".accdb", ".rar", ".zip", ".7z"]


# Проверяем есть ли в папке загрузок <>файлы. Если есть, кидаем их в папку <>
def move_files(downloads_files, file_format, downloads_path, format_folder):
    for name_file in downloads_files:
        if name_file.endswith(file_format):
            os.rename(downloads_path + name_file, format_folder + name_file)


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
    # Путь вида /домашняяпапка/имяпользователя
    if type_os == "Linux":
        default_path_u = "/home/" + usermane + "/"
    else:
        default_path_u = r"C:/Users/" + usermane + r"/"
    #Путь до папки с загрузками
    default_path_d = default_path_u + user_downloads_path + "/"
    #Задаём путь к папке с загрузками для конкретного пользователя
    downloads_path = os.listdir(default_path_d)
    #Проверяем есть ли в папке загрузок видеофайлы. Если есть, кидаем их в папку Видео
    for video_format in video_formats:
        if type_os == "Linux":
            move_files(downloads_path, video_format, default_path_d, default_path_u + "Видео/")
        if type_os == "Windows":
            move_files(downloads_path, video_format, default_path_d, default_path_u + "Videos/")
    #Проверяем есть ли в папке загрузок аудиофайлы. Если есть, кидаем их в папку Музыка
    for music_format in music_formats:
        if type_os == "Linux":
            move_files(downloads_path, music_format, default_path_d, default_path_u + "Музыка/")
        if type_os == "Windows":
            move_files(downloads_path, music_format, default_path_d, default_path_u + "Music/")
    #Проверяем есть ли в папке загрузок изображения. Если есть, кидаем их в папку Изображения
    for pic_format in pic_formats:
        if type_os == "Linux":
            move_files(downloads_path, pic_format, default_path_d, default_path_u + "Изображения/")
        if type_os == "Windows":
            move_files(downloads_path, pic_format, default_path_d, default_path_u + "Pictures/")
    #Проверяем есть ли в папке загрузок документы или архивы. Если есть, кидаем их в папку Документы
    for doc_format in doc_formats:
        if type_os == "Linux":
            move_files(downloads_path, doc_format, default_path_d, default_path_u + "Документы/")
        if type_os == "Windows":
            move_files(downloads_path, doc_format, default_path_d, default_path_u + "Documents/")
    #Запрос на удаление оставшихся файлов в директории загрузок
    delete_user_confirm = input('Удалить из папки загрузок оставшиеся файлы? Напишите да или нет (по-умолчанию: нет) ' or 'нет')
    if delete_user_confirm == 'да':
        if type_os == "Linux":
            files_to_remove = os.listdir(default_path_d)
            for remove_files in files_to_remove:
                os.remove(default_path_d + "/" + remove_files)
        if type_os == "Windows":
            files_to_remove = os.listdir(default_path_d)
            for remove_files in files_to_remove:
                os.remove(default_path_d + "/" + remove_files)
    else:
        print('Программа завершила работу. Все файлы размещены.')


if __name__ == '__main__':
    main()
