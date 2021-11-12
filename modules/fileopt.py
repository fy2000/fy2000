# -*- coding: utf-8 -*-
import os


def check_file_extension(filename, f_ext):
    if (not filename) or (not f_ext):
        return True
    else:
        (t_name, t_ext) = os.path.splitext(filename)
        if t_ext == f_ext:
            return True
        else:
            return False


def list_file(filepath, file_extension=''):
    if not os.path.exists(filepath):
        print("file path is not exist! --> [", filepath, "]")
        return []

    max_index = len(filepath) - 1
    last_char = filepath[max_index]
    filepath = filepath[:max_index] if last_char == '\\' or last_char == '/' else filepath
    list_files = list()
    for root, dirs, files in os.walk(filepath):
        for filename in files:
            file_all_path = root + '\\' + filename
            if check_file_extension(filename, file_extension):
                list_files.append(file_all_path)

    return list_files
