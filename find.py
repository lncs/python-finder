# coding=utf-8
import os
import re

from logpublic import *
'''
2019-04-23
使用try保证可以打开文件，不用传入文件的具体编码格式，程序中做兼容处理

2019-06-13
查询结果存放在工具所在路径下，和选择的文件夹无关
'''


def find(path, suffix, content, encodingformat='utf8'):
    app_logger.info('入参为【路径:{},文件后缀:{},查询内容:{}】'.format(path, suffix, content))

    app_logger.debug('清空【result.txt】文件内容')
    result_file = open('result.txt', 'w+')
    result_file.truncate()  # 清空文件内容

    # 查询内容使用模糊匹配
    find_str = content + ".*"

    for root, dirs, files in os.walk(path):
        for name in dirs:
            pass
        for name in files:
            # 遍历文件需要排除生成的结果文件，避免死循环
            if name == 'result.txt':
                continue
            if name.endswith(suffix):
                filename = root + "/" + name
                print(filename)
                try:
                    app_logger.debug('默认以uft-8编码打开文件【{}】'.format(name))
                    with open(filename, 'r', encoding='utf8') as f:

                        i = 1
                        while 1:
                            try:
                                line = f.readline()
                            except Exception as e:
                                app_logger.error('抛出异常:{}'.format(e))
                                raise

                            result = re.findall(find_str, line, re.IGNORECASE)

                            if result:
                                # 模糊匹配，关键字所在的行
                                res = str(line)
                                # 精细匹配，关键字开始当行尾
                                # res = str(i)+':'+str(result[0]) + '\n'
                                res = root + '/' + name + ':' + res
                                # print (res)

                                f1 = open('result.txt', 'a', encoding='utf-8')
                                f1.write(res)
                                f1.close()
                            i = i + 1
                            if not line:
                                break
                except Exception as e:
                    app_logger.debug('使用uft-8格式打开文件【{}】失败，以gbk方式打开'.format(name))
                    with open(filename, 'r') as f:
                        i = 1
                        while 1:
                            try:
                                line = f.readline()
                            except Exception as e:
                                # 当使用gbk编码也打开失败之后，记录日志不抛出异常
                                app_logger.error('异常:{},请注意文件【{}】编码格式'.format(e, filename))
                                # raise

                            result = re.findall(find_str, line, re.IGNORECASE)

                            if result:
                                # 模糊匹配，关键字所在的行
                                res = str(line)
                                # 精细匹配，关键字开始当行尾
                                # res = str(i)+':'+str(result[0]) + '\n'
                                res = root + '/' + name + ':' + res
                                # print (res)

                                f1 = open('result.txt', 'a', encoding='utf-8')
                                f1.write(res)
                                f1.close()
                            i = i + 1
                            if not line:
                                break


if __name__ == '__main__':
    find("./dist", "", "测试")
