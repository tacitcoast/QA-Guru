import os
import pytest

path_tmp = os.path.abspath(os.path.join(os.path.dirname(__file__), '../tmp'))
path_res = os.path.abspath(os.path.join(os.path.dirname(__file__), '../resources'))


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    for f in os.listdir(path_tmp):
        os.remove(os.path.join(path_tmp, f))