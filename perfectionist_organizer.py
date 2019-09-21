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


# Справшиваем у юзверя, как называется папка с загрузками (по-умолчанию: Загрузки)
def get_user_downloads_path(type_os):
    if type_os == "Linux":
        return input("Как у вас называется папка с загрузками? (по-умолчанию: Загрузки) ") or "Загрузки"
    if type_os == "Windows":
        return input("Как у вас называется папка с загрузками? (по-умолчанию: Загрузки) ") or "Downloads"


# Проверяем есть ли в папке загрузок <>файлы. Если есть, кидаем их в папку <>
def move_files(downloads_files, file_format, downloads_path, format_folder):
    for name_file in downloads_files:
        if name_file.endswith(file_format):
            os.rename(downloads_path + name_file, format_folder + name_file)


def main():
    #Проверка операционной системы, которой пользуется юзер
    type_os = platform.system()
    user_downloads_path = get_user_downloads_path(type_os)
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

    folders = {}
    if type_os == "Linux":
        folders = {"Видео/": video_formats, "Музыка/": music_formats, "Изображения/": pic_formats, "Документы/": doc_formats}
    if type_os == "Windows":
        folders = {"Videos/": video_formats, "Music/": music_formats, "Pictures/": pic_formats, "Documents/": doc_formats}
    for format_folder, file_formats in folders:
        for file_format in file_formats:
            move_files(downloads_path, file_format, default_path_d, default_path_u + format_folder)

    #Запрос на удаление оставшихся файлов в директории загрузок
    delete_user_confirm = input('Удалить из папки загрузок оставшиеся файлы? Напишите да или нет (по-умолчанию: нет) ' or 'нет')
    if delete_user_confirm == 'да':
        files_to_remove = os.listdir(default_path_d)
        for remove_files in files_to_remove:
            os.remove(default_path_d + "/" + remove_files)
    else:
        print('Программа завершила работу. Все файлы размещены.')


if __name__ == '__main__':
    main()
