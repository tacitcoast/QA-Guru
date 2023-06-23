with open('hello.txt', 'w') as file:
    file.write('Hello!\nWorld\n')
    file.writelines(['Hello', "Anybody"])
    file.writelines(['Hello', "Anybody"])

with open('hello.txt') as file:
    text = file.read()
    print(text)

with open('hello2.txt', 'x') as file:
    file.write('abc')

with open('hello.txt', 'a') as file:
    file.write('\nA - for appending')
