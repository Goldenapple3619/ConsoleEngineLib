def check_index(array, index) -> bool:
    try:
        if type(index) == tuple or type(index) == list:
            array[index[0]][index[1]]
        else:
            array[index]
        return True
    except IndexError:
        return False

def check_file_exist(file_path) -> bool:
    from os.path import isfile

    return True if isfile(file_path) else False

def check_folder_exist(folder_path) -> bool:
    from os.path import isdir

    return True if isdir(folder_path) else False

def check_none(obj) -> bool:
    return True if obj is None else False