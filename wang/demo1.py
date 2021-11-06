
import os
import matplotlib.pyplot as plt
import cv2

BASE_DIR = os.path.dirname(os.path.abspath(__file__)) + "/images/"


class Solution_d1:
    def __init__(self):
        pass

    def _func(self,**kwargs):
        '''
        内部的自定义函数股，返回自己需要的结果，没有用到内部函数就不写
        :param kwargs:  关键子传参数
        :return:
        '''
        pass


    def run_d1(self):
        '''
        写具体的逻辑
        :param kwargs: 接收得所有关键字传参
        :return:
        '''
        while True:
            pic_name =  input('请输入图片名<需要加图片格式后缀>：')
            filename = BASE_DIR + pic_name
            if os.path.exists(filename):
                img = cv2.imread(filename,1)
                cv2.waitKey(1)
                plt.imshow(img)
                plt.show()
            else:
                print("当前文件不存在，请确认后重新输入")
                continue
            tmp = input('是否继续当前选项：Y/N')
            if tmp == 'Y':
                continue
            else:
                break


class Solution_d2:
    def __init__(self):
        pass

    def _func(self, **kwargs):
        '''
        内部的自定义函数股，返回自己需要的结果
        :param kwargs:  关键子传参数
        :return:
        '''
        pass

    def run_d2(self):
        '''
        写选项2逻辑
        :param kwargs: 接收得所有关键字传参
        :return:
        '''
        pass

class Solution_d3:
    def __init__(self):
        pass

    def _func(self, **kwargs):
        '''
        内部的自定义函数股，返回自己需要的结果
        :param kwargs:  关键子传参数
        :return:
        '''
        pass

    def run_d3(self):
        '''
        写选项2逻辑
        :param kwargs: 接收得所有关键字传参
        :return:
        '''
        pass

class Solution_d4:
    def __init__(self):
        pass

    def _func(self, **kwargs):
        '''
        内部的自定义函数股，返回自己需要的结果
        :param kwargs:  关键子传参数
        :return:
        '''
        pass

    def run_d4(self):
        '''
        写选项2逻辑
        :param kwargs: 接收得所有关键字传参
        :return:
        '''
        pass


class Solution_d5:
    def __init__(self):
        pass

    def _func(self, **kwargs):
        '''
        内部的自定义函数股，返回自己需要的结果
        :param kwargs:  关键子传参数
        :return:
        '''
        pass

    def run_d5(self):
        '''
        写选项2逻辑
        :param kwargs: 接收得所有关键字传参
        :return:
        '''
        pass


class Solution_d6:
    def __init__(self):
        pass

    def _func(self, **kwargs):
        '''
        内部的自定义函数股，返回自己需要的结果
        :param kwargs:  关键子传参数
        :return:
        '''
        pass

    def run_d6(self):
        '''
        写选项2逻辑
        :param kwargs: 接收得所有关键字传参
        :return:
        '''
        pass


class Solution_d7:
    def __init__(self):
        pass

    def _func(self, **kwargs):
        '''
        内部的自定义函数股，返回自己需要的结果
        :param kwargs:  关键子传参数
        :return:
        '''
        pass

    def run_d7(self):
        '''
        写选项2逻辑
        :param kwargs: 接收得所有关键字传参
        :return:
        '''
        pass


class Solution_d8:
    def __init__(self):
        pass

    def _func(self, **kwargs):
        '''
        内部的自定义函数股，返回自己需要的结果
        :param kwargs:  关键子传参数
        :return:
        '''
        pass

    def run_d8(self):
        '''
        写选项2逻辑
        :param kwargs: 接收得所有关键字传参
        :return:
        '''
        pass


class Solution_d9:
    def __init__(self):
        pass

    def _func(self, **kwargs):
        '''
        内部的自定义函数股，返回自己需要的结果
        :param kwargs:  关键子传参数
        :return:
        '''
        pass

    def run_d9(self):
        '''
        写选项2逻辑
        :param kwargs: 接收得所有关键字传参
        :return:
        '''
        pass