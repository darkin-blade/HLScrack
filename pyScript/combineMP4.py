import os
import sys

if __name__ == '__main__':
    fdNew = open("combined.aac", "xb") # x: 如果文件存在则返回错误
    for i in range(100):
        filename = "test_1/{}.aac".format(i)
        if not os.path.exists(filename):
            break
        print(filename)
        # 打开文件
        fd = open(filename, "rb")
        while True:
            data = fd.read(1024)
            if data == b'':
                # 文件末尾
                break
            fdNew.write(data)
        fd.close()
    fdNew.close()
    fdNew = open("combined.mp4", "xb") # x: 如果文件存在则返回错误
    for i in range(100):
        filename = "test_1/{}.mp4".format(i)
        if not os.path.exists(filename):
            break
        print(filename)
        # 打开文件
        fd = open(filename, "rb")
        while True:
            data = fd.read(1024)
            if data == b'':
                # 文件末尾
                break
            fdNew.write(data)
        fd.close()
    fdNew.close()
