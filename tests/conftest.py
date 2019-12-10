from pytest import fixture

from selenium import webdriver

from config import Config

#be sure to download webdrivers ahead of time to run locally
@fixture(params=[webdriver.Chrome, webdriver.Safari])
def browser(request):
    driver = request.param
    drvr = driver()
    yield drvr
    drvr.quit()

@fixture
def chrome_browser():
    browser = webdriver.Chrome()
    return browser

@fixture
def safari_browser():
    browser = webdriver.Safari()
    return browser

def pytest_addoption(parser):
    parser.addoption(
        "--env", 
        action="store", 
        help="Environment to run tests against"
    )
    
@fixture(scope='session')
def env(request):
    return request.config.getoption("--env")

@fixture(scope='session')
def app_config(env):
    cfg = Config(env)
    return cfg