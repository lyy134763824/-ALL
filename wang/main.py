import os
import sys
from demo1 import *
'''
    |10.文字显示出处理过程                   |
    |11.显示并保存处理结果等                  |
10/11建议做图像模块项目都加
'''
#配置环境路径 把当前项目文件夹配置到系统路径中
py_path = os.path.abspath(__file__)
py_dir_path = os.path.dirname(py_path)
py_pre_dir_path = os.path.dirname(py_dir_path)
sys.path.append(py_pre_dir_path)

class Solution_main:
    def __init__(self):
        #引入其他实例类
        self.d1 = Solution_d1()
        self.d2 = Solution_d2()
        self.d3 = Solution_d3()
        self.d4 = Solution_d4()
        self.d5 = Solution_d5()
        self.d6 = Solution_d6()
        self.d7 = Solution_d7()
        self.d8 = Solution_d8()
        self.d9 = Solution_d9()


    def run(self,):
        while True:
            num = input(
'''
|------------------------------------|
|请输入选项：                           |
|1.输入文件名，读取并显示图像             |
|2.旋转图像                            |
|3.缩放图像                            |
|4.若是灰度图像反相处理                  |
|5.水平反转图像                         |
|6.上下反转图像                         |
|7.提取图像中的轮廓                      |
|8.直方图均衡化                         |
|9.输入不同参数，控制均值滤波、高斯滤波强度  |
|--------------------------------------|
''')
            if not num.isdigit():
                num2 = input('输入有误，是否继续Y/N：')
                if num2 == 'Y':
                    continue
                else:
                    break
            else:
                if   int(num) < 1 or int(num) > 9:
                    print('请输入指定选项：')
                    continue
                else:
                    if num == "1":
                        self.d1.run_d1()
                    elif num == '2':
                        self.d2.run_d2()
                    elif num == '3':
                        self.d3.run_d3()
                    elif num == '4':
                        self.d4.run_d4()
                    elif num == '5':
                        self.d5.run_d5()
                    elif num == '6':
                        self.d6.run_d6()
                    elif num == '7':
                        self.d7.run_d7()
                    elif num == '8':
                        self.d8.run_d8()
                    elif num == '9':
                        self.d9.run_d9()

if __name__ == '__main__':
    S = Solution_main()
    S.run()
