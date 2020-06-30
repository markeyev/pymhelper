# coding: utf-8

# pylint: disable=missing-module-docstring
# pylint: disable=missing-function-docstring

import os
from pymhelper.files import get_file_last_line


def test_get_file_last_line():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    filename = os.path.join(dir_path, 'data', 'test.txt')
    assert get_file_last_line(filename) == ('alias consequatur aut perferendis'
                                            ' doloribus asperiores repellat…')
