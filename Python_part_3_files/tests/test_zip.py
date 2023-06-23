import os
import zipfile
from zipfile import ZipFile


def test_create_and_add_archive():
    path_tmp = os.path.dirname(os.path.abspath(__file__)) + '/../tmp'
    path_res = os.path.dirname(os.path.abspath(__file__)) + '/../resources'
    file_dir = os.listdir(path_res)

    with zipfile.ZipFile(path_tmp + '/test.zip', mode='w', \
                         compression=zipfile.ZIP_DEFLATED) as zf:
        for file in file_dir:
            add_file = os.path.join(path_res, file)
            zf.write(add_file)


def test_read_archive():
    path_res = os.path.dirname(os.path.abspath(__file__)) + '/../resources'
    path_tmp = os.path.dirname(os.path.abspath(__file__)) + '/../tmp'
    with ZipFile(path_tmp + '/test.zip') as zf:
        filenames = [os.path.basename(file) for file in zf.namelist()]
        print(filenames)
        print(os.listdir(path_res))
        assert filenames == os.listdir(path_res)
