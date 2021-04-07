import pytest
import allure
def inc(x):
    return x+2

def test_inc():
    assert inc(1)   == 4
class Testadd:
    def setup(self):
        print("setup")
    @pytest.mark.success
    def test_demo1(self):
        assert inc(1) == 3

    @pytest.mark.failed
    def test_demo2(self):
        assert inc(2) == 5

    @pytest.mark.parametrize("data,expect",[
        (1,2),
        (3,4),
        (10,11),
    ])
    def test_data(self,data,expect):
        allure.attach("this is text",attachment_type=allure.attachment_type.TEXT)
        # allure.attach('this is html ',attachment_type=allure.attachment_type.HTML)
        allure.attach('<img src="https://www.testing-studio.com/wp-content/uploads/2019/11/4-必备实战大纲-3.jpg" alt="" class="wp-image-2602" srcset="https://www.testing-studio.com/wp-content/uploads/2019/11/4-必备实战大纲-3.jpg 1200w, https://www.testing-studio.com/wp-content/uploads/2019/11/4-必备实战大纲-3-300x204.jpg 300w, https://www.testing-studio.com/wp-content/uploads/2019/11/4-必备实战大纲-3-768x522.jpg 768w, https://www.testing-studio.com/wp-content/uploads/2019/11/4-必备实战大纲-3-1024x695.jpg 1024w" sizes="(max-width: 1200px) 100vw, 1200px">',attachment_type=allure.attachment_type.HTML)
        assert inc(data) == expect


    def teardown(self):
        print("teardown")
