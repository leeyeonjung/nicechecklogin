import pytest
from configuration import webDriver
import Logic.common as cm
import Logic.agency as ac
import testData.test_data as test_data

class Test_KakaoAgency:
    @pytest.fixture
    def setup(self):
        pass

    def test_startApp(self):
        webDriver.cal()

    def test_intoMerchant(self):
        ac.intoAgency()

    def test_kakao(self):
        cm.kakaoLoginClick()
        cm.kakaoLoginLogic(test_data.sign_kakao[0])

    def test_confirmAgency(self):
        ac.confirmAgency(test_data.agency_biz_no[0])

    def test_recordExcel(self):
        cm.recordResult(('//main/div/div[1]/div/div[2]/div/p'), '누적회원가입수', 'login', 2, 4)

    def test_resign(self):
        ac.resign()

class Test_PhoneAgency:
    @pytest.fixture
    def setup(self):
        pass

    def test_startApp(self):
        webDriver.cal()

    def test_intoMerchant(self):
        ac.intoAgency()

    def test_phoneLogin(self):
        cm.phoneNumberLoginclick()
        cm.phoneNumberLoginLogic(test_data.sign_phone[0])

    def test_confirmAgency(self):
        ac.confirmAgency(test_data.agency_biz_no[0])

    def test_recordExcel(self):
        cm.recordResult(('//main/div/div[1]/div/div[2]/div/p'), '누적회원가입수', 'login', 2, 5)

    def test_resign(self):
        ac.resign()