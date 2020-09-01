#测试代码
import allure
import pytest
import sys

from LaGouDemo.pythoncode.Calculator import Calc

sys.path.append('..')


class TestCalc:
    def setup_class(self):
        print('在整个类的执行之前执行setup_class')
        self.Cal = Calc()

    def teardown_class(self):
        print('在整个类的执行之后执行teardown_class')

    @pytest.mark.parametrize('a,b,c',[
        (1,1,2),
        (0.1,0.1,0.2),
        (-1,-1,-2),
        (100,100,200),
        (100,-100,0)
        ])
    def test_add(self,a,b,c):
        # cal = Calc()
        allure.attach('这是一个相加的测试用例',name='这是文本型',
                      attachment_type=allure.attachment_type.TEXT)
        allure.attach('<img src="https://ceshiren.com/uploads/default/original/2X/e/e0e12ce7c8e9b941fa14d36bcf4562c873617d9b.jpeg">',name='html类型',
                      attachment_type=allure.attachment_type.HTML)
        assert c == self.cal.add(a,b)

    def test_image(self):
        allure.attach.file('/Users/x/Desktop/123.jpg',
                           name='图片',attachment_type=allure.attachment_type.JPG)
        allure.attach.file('/Users/x/Downloads/新片场素材/a7m4.mp4',
                           name='视频', attachment_type=allure.attachment_type.MP4)
    # def test_add1(self):
    #     cal = Calc()
    #     assert 0.2 == cal.add(0.1,0.1)
    #
    # def test_add2(self):
    #     cal = Calc()
    #     assert -2 == cal.add(-1,-1)


