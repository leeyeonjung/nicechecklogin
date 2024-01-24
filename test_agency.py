import Logic.common
import Logic.agency
import test_data
from configuration import webDriver

webDriver.cal()

Logic.agency.intoAgency()
Logic.common.kakaoLoginClick()
#sign_kakao(email, password)
Logic.common.kakaoLoginLogic(test_data.sign_kakao[0])
print(test_data.sign_kakao[0])
#agency_biz_no (biz_no1, biz_no2)
Logic.agency.confirmAgency(test_data.agency_biz_no[0])
print(test_data.agency_biz_no[0])
Logic.agency.resign()

webDriver.wd.close_app()
webDriver.wd.launch_app()

Logic.agency.intoAgency()
Logic.common.phoneNumberLoginclick()
#sign_phone(name, email, phonenumber)
Logic.common.phoneNumberLoginLogic(test_data.sign_phone[0])
print((test_data.sign_phone[0]))
#agency_biz_no (biz_no1, biz_no2)
Logic.agency.confirmAgency(test_data.agency_biz_no[0])
print(test_data.agency_biz_no[0])
Logic.agency.resign()

webDriver.wd.quit()