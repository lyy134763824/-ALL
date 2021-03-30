def inc(x):
    return x+2

def test_inc():
    assert inc(1)   == 4
class Testadd:
    def setup(self):
        print("setup")
    def test_demo1(self):
        assert inc(1) == 3
    def teardown(self):
        print("teardown")
    def test_demo2(self):
        assert inc(2) == 5

