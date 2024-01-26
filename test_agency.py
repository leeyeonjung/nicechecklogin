import Logic.common
import Logic.agency
import test_data
from configuration import webDriver

webDriver.cal()

try:
    Logic.agency.intoAgency()
    Logic.common.kakaoLoginClick()
    Logic.common.kakaoLoginLogic(test_data.sign_kakao[0])
    Logic.agency.confirmAgency(test_data.agency_biz_no[0])
    Logic.common.recordPassResult(('//main/div/div[1]/div/div[2]/div/p'), '누적회원가입수', 'login', 2, 4)
    Logic.agency.resign()
except Exception as e:
    Logic.common.recordFailResult(('//main/div/div[1]/div/div[2]/div/p'), '누적회원가입수','login', 2, 4)
    pass

webDriver.wd.close_app()
webDriver.wd.launch_app()

try:
    Logic.agency.intoAgency()
    Logic.common.phoneNumberLoginclick()
    #sign_phone(name, email, phonenumber)
    Logic.common.phoneNumberLoginLogic(test_data.sign_phone[0])
    print((test_data.sign_phone[0]))
    #agency_biz_no (biz_no1, biz_no2)
    Logic.agency.confirmAgency(test_data.agency_biz_no[0])
    print(test_data.agency_biz_no[0])
    Logic.common.recordPassResult(('//main/div/div[1]/div/div[2]/div/p'), '누적회원가입수', 'login', 2, 5)
    Logic.agency.resign()
except Exception as e:
    Logic.common.recordFailResult(('//main/div/div[1]/div/div[2]/div/p'), '누적회원가입수', 'login', 2, 5)
    pass

webDriver.wd.quit()