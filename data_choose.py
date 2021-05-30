import os
import random

'''import xml.etree.cElementTree as et
from os import listdir, path'''
""" 2020年7月8日 """


class data_choose():
    # data_choose
    def Random_choose(self, number):
        rootdir = os.getcwd() + "\VOCtrainval_11-May-2012\VOCdevkit\VOC2012\Annotations"
        file_names = []
        file_list = []
        for parent, dirnames, filenames in os.walk(rootdir):  # 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
            file_names = filenames
        x = [random.randint(0, len(file_names) - 1) for _ in range(number)]
        for i in x:
            file_list.append(file_names[i])
            # print(file_names[i])
        return file_list
        # print(type(x))
        # print(file_names)

    def test(self, number):
        print("随机选取：", data_choose.Random_choose(self, number))


if __name__ == '__main__':
    data_choose().test(1)
