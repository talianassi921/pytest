from pytest import mark

@mark.body
class BodyTests:
    @mark.ui
    def test_can_navigate_to_body_page(self):
        assert True
        
    def test_bumper(self):
        assert True
        
    def windshield(self):
        assert True