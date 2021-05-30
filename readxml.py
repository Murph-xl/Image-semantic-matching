import xml.etree.cElementTree as et
from data_choose import *

'''
调用xml库中的相关方法可以快速实现xml文件中的信息的读取
此处读取的xml文件的格式为VOC中的数据标注格式，以下脚本展示了
读取所有的bounding box的坐标的方法，相应的可以按照以下方式
读取其他的信息。
'''


# print(a)
# print(type(a))
class readxml():
    def readxml(self, str1):
        #str_root = 'D:\\Laboratory\\Image semantic matching\\VOCtrainval_11-May-2012\\VOCdevkit\\VOC2012\\Annotations\\'
        #str_xml = open(str_root + str1, 'r').read()
        str_xml = open(self.readfile(str1)).read()
        root = et.XML(str_xml)
        name_list = []
        for Object in root.findall('object'):
            name = Object.find('name').text
            name_list.append(name)
        while len(name_list):
            if len(name_list) < 5:
                name_list.append('')
            else:
                name_list = name_list[: 5]
            break
        return name_list

    def readfile(self, str):
        path = os.getcwd()  # 获取程序所在文件夹路径
        # 'D:\\Laboratory\\Image semantic matching\\VOCdevkit\\VOC2012\\Annotations'
        #list = os.listdir(path)  # 获取指定路径下的所有文件的文件名称
        #print(list)
        for dirpath, dirnames, filenames in os.walk(path):
            for filename in filenames:
                if filename == str:
                    #print(os.path.join(dirpath, filename))
                    return os.path.join(dirpath, filename)

    def test(self):
        print(readxml().readxml("2007_000027.xml"))


if __name__ == '__main__':
    readxml().test()
