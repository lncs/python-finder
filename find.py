# coding=utf-8
import os
import re

'''
2019-04-23
使用try保证可以打开文件，不用传入文件的具体编码格式，程序中做兼容处理
'''


def find(path, suffix, content, encodingformat='utf8'):
    # print("入参path["+str(path) +"],suffix[" + str(suffix) + "],content[" + str(content)+"]")
    # 清空文件
    resultFile = open(path + '/result.txt', 'w+')
    resultFile.truncate()  # 清空文件内容

    # 查询内容使用模糊匹配
    findStr = content + ".*"

    for root, dirs, files in os.walk(path):
        for name in dirs:
            pass
        for name in files:
            # 遍历文件需要排除生成的结果文件，避免死循环
            if name == 'result.txt':
                continue
            if name.endswith(suffix):
                filename = root + "/" + name
                try:
                    with open(filename, 'r', encoding='utf8') as f:

                        i = 1
                        while 1:
                            try:
                                line = f.readline()
                            except Exception as e:
                                raise

                            result = re.findall(findStr, line, re.IGNORECASE)

                            if result:
                                # 模糊匹配，关键字所在的行
                                res = str(line)
                                # 精细匹配，关键字开始当行尾
                                # res = str(i)+':'+str(result[0]) + '\n'
                                res = root + '/' + name + ':' + res
                                # print (res)

                                f1 = open(path + '/result.txt', 'a', encoding='utf-8')
                                f1.write(res)
                                f1.close()
                            i = i + 1
                            if not line:
                                break
                except:
                    with open(filename, 'r') as f:
                        i = 1
                        while 1:
                            try:
                                line = f.readline()
                            except Exception as e:
                                raise

                            result = re.findall(findStr, line, re.IGNORECASE)

                            if result:
                                # 模糊匹配，关键字所在的行
                                res = str(line)
                                # 精细匹配，关键字开始当行尾
                                # res = str(i)+':'+str(result[0]) + '\n'
                                res = root + '/' + name + ':' + res
                                # print (res)

                                f1 = open(path + '/result.txt', 'a', encoding='utf-8')
                                f1.write(res)
                                f1.close()
                            i = i + 1
                            if not line:
                                break


if __name__ == '__main__':
    find("./dist", ".txt", "ne")
