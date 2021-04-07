# import unittest
#
#
# class MyTestCase(unittest.TestCase):
#     def test_something(self):
#         self.assertEqual(True, True)
#
#
# if __name__ == '__main__':
#     unittest.main()
m = [lambda x:x*i for i in range(3)]
for m in m:
    print(m(1))



# def my(func):
#     def inner(*agrs,**kwargs):
#         inner.i+=1
#         return func(*agrs,**kwargs)
#     inner.i = 0
#     return inner
# @my
# def text():
#     pass
# text()
# text()
# text()
# print(text.i)


