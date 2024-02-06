def read_file():
    helloFile = open('test_files/hello.txt')
    print(helloFile.readlines())
    print(helloFile.read())
    print(helloFile.readline())


def write_file():
    w1File = open('test_files/w1.txt', 'w')
    res = w1File.write('HELLO Luca\n')  # 写入的字符个数
    print(res)


def append_file():
    w2File = open('test_files/w2.txt', 'a')
    res = w2File.write('HELLO Luca\n')
    print(res)


if __name__ == '__main__':
    read_file()
    # write_file()
    # append_file()

