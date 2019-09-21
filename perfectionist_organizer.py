#Импорт необходимых библиотек
import os
import platform
from pathlib import Path

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
    elif type_os == "Windows":
        return input("Как у вас называется папка с загрузками? (по-умолчанию: Загрузки) ") or "Downloads"


# Проверяем есть ли в папке загрузок <>файлы. Если есть, кидаем их в папку <>
def move_files(downloads_path, file_formats, format_folder):
    for name_file in downloads_path.iterdir():
        if name_file.suffix() in file_formats:
            os.rename(downloads_path / name_file, format_folder / name_file)


def main():
    #Проверка операционной системы, которой пользуется юзер
    type_os = platform.system()
    if type_os not in ("Linux", "Windows"):
        return
    user_downloads_path = get_user_downloads_path(type_os)
    # Путь вида /домашняяпапка/имяпользователя
    default_path_u = Path.home()
    #Путь до папки с загрузками
    default_path_d = default_path_u / user_downloads_path

    if type_os == "Linux":
        folders = {"Видео/": video_formats, "Музыка/": music_formats, "Изображения/": pic_formats, "Документы/": doc_formats}
    else:
        folders = {"Videos/": video_formats, "Music/": music_formats, "Pictures/": pic_formats, "Documents/": doc_formats}
    for format_folder, file_formats in folders:
        move_files(default_path_d, file_formats, default_path_u / format_folder)

    #Запрос на удаление оставшихся файлов в директории загрузок
    delete_user_confirm = input('Удалить из папки загрузок оставшиеся файлы? Напишите да или нет (по-умолчанию: нет) ' or 'нет')
    if delete_user_confirm == 'да':
        for remove_files in default_path_d.iterdir():
            os.remove(default_path_d / remove_files)
    else:
        print('Программа завершила работу. Все файлы размещены.')


if __name__ == '__main__':
    main()
