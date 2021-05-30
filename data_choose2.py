import os
'''import xml.etree.cElementTree as et
from os import listdir, path'''


class data_choose2():

    def Orientation_choose(self, first, after):
        rootdir = os.getcwd()+"\VOCtrainval_11-May-2012\VOCdevkit\VOC2012\Annotations"
        file_names = []
        file_list = []
        for parent, dirnames, filenames in os.walk(rootdir):  # 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
            file_names = filenames
        t = first  # 从第几个文件开始
        k = after  # 查找多少个文件
        n = 1
        while n <= k:
            t = t + 1
            n = n + 1
            # print(t)
            if t > 17124:
                t = 0
            file_list.append(file_names[t])
        return file_list

    def test(self, number1, number2):
        print("定向选取：", data_choose2.Orientation_choose(self, number1, number2))


if __name__ == '__main__':
    data_choose2().test(-1, 2)
