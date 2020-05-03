# -*- coding: utf-8 -*-

import chardet
import os

'''
1.关键字
2.主文件的路径


1.循环遍历打开子文件
2.打开文件中的.h .hpp .cpp .c文件
3.找到文件中需要搜索的关键字并输出行号

'''
keyword1 = 'eval_kfm'
keyword2 = 'pow'
keyword3 = '()'
dirlist = r'C:\Users\wlp\Desktop\周老师交流\2020_3_3\src'

# 遍历文件夹
def walkFile(file):

    count_dir = 0 #文件数量

    # 获取文件编码类型
    def get_encoding(file):
        # 二进制方式读取，获取字节数据，检测类型
        with open(file, 'rb') as f:
            data = f.read()
            return chardet.detect(data)['encoding']



    #遍历文件
    for root, dirs, files in os.walk(file):
        # root 表示当前正在访问的文件夹路径
        # dirs 表示该文件夹下的子目录名list
        # files 表示该文件夹下的文件list
        # 遍历文件
        for f in files:

            if(f[-4:]=='.hpp' or f[-4:]=='.cpp'or f[-2:]=='.h'or f[-2:]=='.c'):

                count_dir += 1
                filename = os.path.join(root, f)
                filename = filename.replace('\\', '/')
                # print(filename)
                # print(get_encoding(filename))#获得文件编码方式
                f = open(filename, 'r',encoding = 'ISO-8859-1')
                # print("文件名为: ", f.name)
                count = 0 #文件中的行数

                for line in f.readlines():  # 依次读取每行
                    count += 1
                    line = line.strip()  # 去掉每行头尾空白
                    # print("读取的数据为: %s" % (line))#每行的数据

                    # if (line.find( keyword1 ) != -1 and line.find( keyword2 ) != -1 and line.find( keyword3 ) != -1):
                    # if (line.find( keyword1 ) != -1 and line.find( keyword2 ) != -1):
                    if (line.find(keyword1) != -1):
                        print("读取的数据为: %s" % (line))#每行的数据
                        print(filename,count)
                        print(" ")
                        # print(count)


                f.close()
    # print(count_dir)
                # print(os.path.join(root, f))
                # print(f)

walkFile(dirlist)


