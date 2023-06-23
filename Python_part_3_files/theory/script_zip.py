from zipfile import ZipFile
zip_ = ZipFile('resources/hello.zip')
print(zip_.namelist())

text = zip_.read('Hello.txt')
print(text)
zip_.close()

with ZipFile('resources/hello.zip') as hellozip:
    hellozip.extract('Hello.txt')
