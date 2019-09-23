# Импорт необходимых библиотек
import argparse
from pathlib import Path
import platform

# Создание списков с расширениями файлов
video_formats = [".3gp", ".avi", ".flv", ".m4v", ".mkv", ".mov", ".mp4", ".wmv", ".webm"]
music_formats = [".mp3", ".aac", ".flac", ".mpc", ".wma", ".wav"]
pic_formats = [".raw", ".jpg", ".tiff", ".psd", ".bmp", ".gif", ".png", ".jp2", ".jpeg"]
doc_formats = [".doc", ".docx", ".txt", ".rtf", ".pdf", ".fb2", ".djvu", ".xls",
               ".xlsx", ".ppt", ".pptx", ".mdb", ".accdb", ".rar", ".zip", ".7z"]


# Спрашиваем у юзверя, как называется папка с загрузками (по-умолчанию: Загрузки)
def get_user_downloads_path(type_os):
    if type_os == "Linux":
        return input("Как у вас называется папка с загрузками? (по-умолчанию: Загрузки) ") or "Загрузки"
    if type_os == "Windows":
        return input("Как у вас называется папка с загрузками? (по-умолчанию: Загрузки) ") or "Downloads"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', action='store_true', dest='delete_rest_files', help='Удалить из папки загрузок оставшиеся файлы')
    args = parser.parse_args()
    # Проверка операционной системы, которой пользуется юзер
    type_os = platform.system()
    if type_os not in ("Linux", "Windows"):
        return
    user_downloads_path = get_user_downloads_path(type_os)
    # Путь вида /домашняяпапка/имяпользователя
    default_path_u = Path.home()
    # Путь до папки с загрузками
    default_path_d = default_path_u / user_downloads_path

    # Создание словарей с расширениями файлов и папкой, куда их нужно перекинуть
    if type_os == "Linux":
        folders = {"Видео": video_formats, "Музыка": music_formats, "Изображения": pic_formats, "Документы": doc_formats}
    else:
        folders = {"Videos": video_formats, "Music": music_formats, "Pictures": pic_formats, "Documents": doc_formats}

    # Проверяем есть ли в папке загрузок файлы определённого формата. Если есть, кидаем их в соответствующую папку
    for format_folder, file_formats in folders.items():
        for name_file in default_path_d.iterdir():
            if name_file.suffix in file_formats:
                name_file.rename(default_path_u / format_folder / name_file.name)

    # Удаление оставшихся файлов в директории загрузок
    if args.delete_rest_files:
        for remove_files in default_path_d.iterdir():
            if remove_files.is_file():
                remove_files.unlink()
    else:
        print('Программа завершила работу. Все файлы размещены.')


if __name__ == '__main__':
    main()
