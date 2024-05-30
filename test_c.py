import pytest
from configuration import webDriver
import Logic.common as cm
import Logic.merchant as mc
import test_data

# try:
class TestReports:
    @pytest.fixture
    def setup(self):
        pass
    def test_startapp(self):
        assert webDriver.cal()

    def test_intoMerchant(self):
        assert mc.intoMerchant()

    def test_kakao(self):
        assert cm.kakaoLoginClick()
        assert cm.kakaoLoginLogic(test_data.sign_kakao[0])

    def test_confirmMerchant(self):
        mc.confirmMerchant()
        mc.passGuidePage()
        cm.recordPassResult(('//main/div/section/section[3]/p'), '매출정산','login', 2, 2)
        mc.resign()
# except Exception as e:
#     cm.recordFailResult(('//main/div/section/section[3]/p'), '매출정산', 'login',2, 2)
#     pass
