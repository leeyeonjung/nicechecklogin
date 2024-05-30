import pytest
from configuration import webDriver
import Logic.common as cm
import Logic.merchant as mc
import testData.test_data as test_data

class Test_KakaoMerchant:
    @pytest.fixture
    def setup(self):
        pass

    def test_startApp(self):
        assert webDriver.cal()

    def test_intoMerchant(self):
        assert mc.intoMerchant()

    def test_kakao(self):
        assert cm.kakaoLoginClick()
        assert cm.kakaoLoginLogic(test_data.sign_kakao[0])

    def test_confirmMerchant(self):
        assert mc.confirmMerchant()

    def test_passGuidePage():
        assert mc.passGuidePage()

    def test_recordExcel(self):
        assert cm.recordResult(('//main/div/section/section[3]/p'), '매출정산','login', 2, 2)

    def test_resign(self):
        assert mc.resign()


class Test_PhoneMerchant:
    @pytest.fixture
    def setup(self):
        pass

    def test_startApp(self):
        assert webDriver.cal()

    def test_intoMerchant(self):
        assert mc.intoMerchant()

    def test_phoneLogin(self):
        assert cm.phoneNumberLoginclick()
        assert cm.phoneNumberLoginLogic(test_data.sign_phone[0])

    def test_confirmMerchant(self):
        assert mc.confirmMerchant()

    def test_passGuidePage():
        assert mc.passGuidePage()

    def test_recordExcel(self):
        assert cm.recordResult(('//main/div/section/section[3]/p'), '매출정산','login', 2, 3)

    def test_resign(self):
        assert mc.resign()
