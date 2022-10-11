from selenium import webdriver
import pytest

# create pytest fixture name call setup
@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    return driver


########### config html report info #############
def pytest_configure(config):
    config._metadata['Project Name'] = 'Guru99 Bank'
    config._metadata['Module'] = 'Login'
    config._metadata['Project Managers'] = 'Login'
    config._metadata['Test Managers'] = 'N/A'
    config._metadata['Tester'] = 'Vannak Tak'
    config._metadata['Developers'] = 'N/A'
