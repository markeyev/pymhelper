"""Files helping functions.
"""
import os


def get_file_last_line(filename: str, max_length: int = 80) -> str:
    """Returns the last line from the file, could be used for big files.

    :param filename:
    :param max_length: limits possible size of last line, by default it is \n
    :return:
    """
    with open(filename, "rb") as f_obj:
        f_obj.seek(-max_length, os.SEEK_END)
        return f_obj.readlines()[-1].decode()
