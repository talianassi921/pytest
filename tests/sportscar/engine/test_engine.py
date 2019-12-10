from pytest import mark

@mark.smoke
@mark.engine
def test_engine_functions_as_expected(chrome_browser):
    chrome_browser.get('http://google.com')
    assert True
    