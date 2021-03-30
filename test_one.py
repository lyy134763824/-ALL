import pytest

def add(x,y):
    return x+y
def test_add_1():
    assert add(1,2)==3
print(test_add_1())
if __name__ == '__main__':
    # pytest.main(['s'],'home/tarena/测试/text_one.py')
    pytest.main()