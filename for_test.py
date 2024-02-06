import os


def for_simple():
    fileNames = ['accounts.txt', 'details.csv', 'invite.docx']
    fileDir = '/usr/bin/spam'
    for fileName in fileNames:
        res = os.path.join(fileDir, fileName)
        print(res)


def for_range():
    fileNames = ['accounts.txt', 'details.csv', 'invite.docx']
    fileDir = '/usr/bin/spam'
    for i in range(len(fileNames)):
        fileName = fileNames[i]
        res = os.path.join(fileDir, fileName)
        print(res)
    for i in range(1, 10, 1):
        print(i)


def for_enumerate():
    """
    获取索引和元素
    """
    fileNames = ['accounts.txt', 'details.csv', 'invite.docx']
    fileDir = '/usr/bin/spam'
    for k, v in enumerate(fileNames):
        res = os.path.join(fileDir, v)
        print(f'i:{k}, res:{res}')


def for_zip():
    fileNames = ['accounts.txt', 'details.csv', 'invite.docx']
    for item1, item2 in zip(fileNames, [fileNames]):
        print(f'{item1}, {item2}')


def for_comprehensions():
    """
    列表推导式
    """
    fileNames = ['accounts.txt', 'details.csv', 'invite.docx']
    fileDir = '/usr/bin/spam'
    res = [os.path.join(fileDir, fileName) for fileName in fileNames]
    # res = [f'{fileDir}/{fileName}' for fileName in fileNames]
    print(res)


if __name__ == '__main__':
    # 打印完整文件路径
    for_simple()
    for_range()
    for_enumerate()
    for_zip()
    for_comprehensions()

