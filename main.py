import os

if __name__ == '__main__':
    # OS X的正斜杠
    # res = os.path.join('usr', 'bin', 'spam')
    # print(res)

    # 获取当前目录
    print(os.getcwd())
    os.chdir('/Users/luca/PycharmProjects/')
    print(os.getcwd())

    # 创建文件夹
    # os.makedirs('/Users/luca/PycharmProjects/pytest/newFolder')

    # 从path2到path1的相对路径
    # res = os.path.relpath('/Users/luca/dev', '/Users/luca/PycharmProjects/pytest/newFolder')
    # print(res)







