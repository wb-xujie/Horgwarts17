# -*- coding: utf-8 -*-
import pytest


class TestCalculater:

    # @pytest.mark.test
    # 这是一个标签
    # 加法测试用例
    def test_add(self,Initialize,get_data_add):
        print("这是加法测试用例")
        print("{0}+{1}={2}".format(get_data_add[0],get_data_add[1],get_data_add[2]))
        assert get_data_add[2] == round(Initialize.add(get_data_add[0],get_data_add[1]),8)


    # @pytest.mark.dev
    # 这是一个标签
    # 除法测试用例
    def test_div(self,Initialize,get_data_div):
        print("这是除法测试用例")
        print("{0}/{1}={2}".format(get_data_div[0], get_data_div[1], get_data_div[2]))
        if get_data_div[1] == 0:
            assert(Initialize.div(get_data_div[0],get_data_div[1])==None)
        else:
            assert get_data_div[2] == round(Initialize.div(get_data_div[0],get_data_div[1]),8)

    # 乘法测试用例
    def test_mul(self,Initialize,get_data_mul):
        print("这是乘法测试用例")
        print("{0}*{1}={2}".format(get_data_mul[0],get_data_mul[1],get_data_mul[2]))
        assert get_data_mul[2] == round(Initialize.mul(get_data_mul[0],get_data_mul[1]),8)


    # 减法测试用例
    def test_sub(self,Initialize,get_data_sub):
        print("这是减法测试用例")
        print("{0}-{1}={2}".format(get_data_sub[0],get_data_sub[1],get_data_sub[2]))
        assert get_data_sub[2] == round(Initialize.sub(get_data_sub[0],get_data_sub[1]),8)

