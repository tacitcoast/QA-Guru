import os
import zipfile
from zipfile import ZipFile
from .conftest import path_tmp, path_res


def test_create_and_add_archive():
    file_dir = os.listdir(path_res)

    with zipfile.ZipFile(os.path.join(path_tmp, 'test.zip'), mode='w', \
                         compression=zipfile.ZIP_DEFLATED) as zf:
        for file in file_dir:
            add_file = os.path.join(path_res, file)
            zf.write(add_file)


def test_read_archive():
    with ZipFile(os.path.join(path_tmp, 'test.zip')) as zf:
        filenames = [os.path.basename(file) for file in zf.namelist()]
        print(filenames)
        print(os.listdir(path_res))
        assert filenames == os.listdir(path_res)
