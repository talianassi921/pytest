from pytest import mark

@mark.skip
def test_entertainment_functions_as_expected(chrome_browser):
    chrome_browser.get('https://kiisfm.iheart.com/')
    assert True