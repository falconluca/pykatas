import shelve


def read():
    """
    读取shelve数据
    """
    db_file = shelve.open('test_files/myDb')
    animals = db_file['animals']
    print(animals)

    names = db_file['names']
    print(names)
    db_file.close()


def write():
    """
    使用shelve保存程序数据
    """
    db_file = shelve.open('myDb')
    animals = ['Cat', 'Simon', 'Falcon']
    db_file['animals'] = animals
    db_file['names'] = ['Luca']
    db_file.close()


if __name__ == '__main__':
    # write()
    read()
