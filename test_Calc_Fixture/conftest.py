# -*- coding: utf-8 -*-

import sys
import pytest

sys.path.append('..')
from Calculater_object.Calculater import *
import yaml


def get_data_func(key, value='value', ids='ids'):
    with open("../test/data.yml") as file:
        data = yaml.safe_load(file)
        data_list = data[key][value]
        ids_list = data[key][ids]
        # print(data)
        return (data_list,ids_list)


@pytest.fixture()
def Initialize():
    calc_function = Calculater()
    print("开始测试")
    yield calc_function
    print("结束测试")


# 这是加法的数据源fixture
@pytest.fixture(params=get_data_func('add')[0],ids=get_data_func('add')[1])
def get_data_add(request):
    return request.param


# 这是除法的数据源fixture
@pytest.fixture(params=get_data_func('div')[0],ids=get_data_func('div')[1])
def get_data_div(request):
    return request.param


# 这是乘法的数据源fixture
@pytest.fixture(params=get_data_func('mul')[0],ids=get_data_func('mul')[1])
def get_data_mul(request):
    return request.param


# 这是减法的数据源fixture
@pytest.fixture(params=get_data_func('sub')[0],ids=get_data_func('sub')[1])
def get_data_sub(request):
    return request.param
