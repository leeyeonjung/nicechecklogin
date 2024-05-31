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
        webDriver.cal()

    def test_intoMerchant(self):
        mc.intoMerchant()

    def test_kakao(self):
        cm.kakaoLoginClick()
        cm.kakaoLoginLogic(test_data.sign_kakao[0])

    def test_confirmMerchant(self):
        mc.confirmMerchant()

    def test_recordExcel(self):
        cm.recordResult(('//main/div/section/section[3]/p'), '매출정산','login', 2, 2)

    def test_resign(self):
        mc.resign()


class Test_PhoneMerchant:
    @pytest.fixture
    def setup(self):
        pass

    def test_startApp(self):
        webDriver.cal()

    def test_intoMerchant(self):
        mc.intoMerchant()

    def test_phoneLogin(self):
        cm.phoneNumberLoginclick()
        cm.phoneNumberLoginLogic(test_data.sign_phone[0])

    def test_confirmMerchant(self):
        mc.confirmMerchant()

    def test_recordExcel(self):
        cm.recordResult(('//main/div/section/section[3]/p'), '매출정산','login', 2, 3)

    def test_resign(self):
        mc.resign()
