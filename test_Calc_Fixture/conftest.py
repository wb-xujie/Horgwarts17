# -*- coding: utf-8 -*-

import sys
import pytest
sys.path.append('..')
from Calculater_object.Calculater import *
import yaml


def get_data_func(key,value = 'value'):
    with open("../test/data.yml") as file:
        data = yaml.safe_load(file)
        # print(data)
        return data[key][value]

@pytest.fixture()
def Initialize():
    calc_function = Calculater()
    print("开始测试")
    yield  calc_function
    print("结束测试")


# 这是加法的数据源fixture
@pytest.fixture(params= get_data_func('add'))
def get_data_add(request):
    return request.param

# 这是除法的数据源fixture
@pytest.fixture(params=get_data_func('div'))
def get_data_div(request):
    return request.param

# 这是乘法的数据源fixture
@pytest.fixture(params=get_data_func('mul'))
def get_data_mul(request):
    return request.param

# 这是减法的数据源fixture
@pytest.fixture(params=get_data_func('sub'))
def get_data_sub(request):
    return request.param