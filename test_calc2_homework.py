"""
课后作业
补全计算器中加法和除法的测试用例
使用参数化完成测试用例的自动生成
在调用测试方法之前打印【开始计算】，在调用测试方法之后打印【计算结束】

注意：
使用等价类，边界值，因果图等设计测试用例
测试用例中添加断言，验证结果
灵活使用 setup(), teardown() , setup_class(), teardown_class()

增加限制条件：
计算后输出长度限制：10**(-8) 到10**8
计算后输出 保留小数点后2位的处理


正常：
    0+0
    0+1
    0+(-1)
    int
输出边界值：len()<=9
    99999999+1
    (-99999999)+(-1)
    float
    99999999.9+0.1
    99999999.9+0.1


输出边界值：len()<=9
    int
    999999999+1
    (-999999999)+(-1)


https://wenku.baidu.com/view/370026aad1f34693daef3eeb.html
https://www.cnblogs.com/fnng/p/4774676.html

"""
import pytest
import yaml

from python_code.calc import Calculator

with open("./datas/calc2.yaml") as f:

    datas = yaml.safe_load(f)
    datas1=datas["add"]
    add_datas_True = datas1["datas_True"]
    add_datas_False = datas1["datas_False"]
    datas2 = datas["div"]
    div_datas_True = datas2["datas_True"]
    div_datas_False = datas2["datas_False"]

class TestCalc2:
    def setup_class(self):
        """
        实例化 计算器类，并且获取yaml文件数据准备后续的参数化
        :return:
        """
        print("开始计算")
        self.calc=Calculator()
    def teardown_class(self):
        print("结束计算")


    @pytest.mark.parametrize(
        'a,b,expect',add_datas_True
                             )
    def test_add_True(self,a,b,expect):
        result=self.calc.add(a,b)
        if isinstance(result,float):
            result=round(result,2)
        assert result==expect
    @pytest.mark.parametrize('a,b,expect',add_datas_False)
    def test_add_Fasle(self,a,b,expect):
        result = self.calc.add(a, b)
        if isinstance(result, float):
            result = round(result,2)
        assert result != expect

    @pytest.mark.parametrize('a,b,expect', div_datas_True)
    def test_div_True(self,a,b,expect):
        if b==0:
            print("被除数不能为0")
            assert False
        else:
            result = self.calc.div(a, b)
            if isinstance(result, float):
                result = round(result,2)
            assert result == expect

    @pytest.mark.parametrize('a,b,expect', div_datas_False)
    def test_div_False(self,a,b,expect):
        if b==0:
            print("被除数不能为0")
            assert False
        else:
            result=self.calc.div(a,b)
            if isinstance(result,float):
                result=round(result,2)
            assert result!=expect

