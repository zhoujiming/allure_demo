import pytest
import allure


@allure.step("步骤1:点xxx")
def step_1():
    print("111")


@allure.step("步骤2:点xxx")
def step_2():
    print("222")


@allure.feature("allure test")
class TestAllure(object):
    @allure.story("allure test 1")
    def test_allure_1(self):
        '''用例描述：allure test 1'''
        step_1()
        step_2()
        assert 1 == 2

    @allure.story("allure test 2")
    def test_allure_2(self):
        '''用例描述：allure test 2'''
        assert 2 == 2
