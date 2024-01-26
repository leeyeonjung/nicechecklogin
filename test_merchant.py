import Logic.common
import Logic.merchant
import test_data
from configuration import webDriver

webDriver.cal()

try:
    Logic.merchant.intoMerchant()
    Logic.common.kakaoLoginClick()
    Logic.common.kakaoLoginLogic(test_data.sign_kakao[0])
    Logic.merchant.confirmMerchant()
    Logic.merchant.passGuidePage()
    Logic.common.recordPassResult(('//main/div/section/section[3]/p'), '매출정산','login', 2, 2)
    Logic.merchant.resign()
except Exception as e:
    Logic.common.recordFailResult(('//main/div/section/section[3]/p'), '매출정산', 'login',2, 2)
    pass


webDriver.wd.close_app()
webDriver.wd.launch_app()

try:
    Logic.merchant.intoMerchant()
    Logic.common.phoneNumberLoginclick()
    #sign_phone(name, email, phonenumber)
    Logic.common.phoneNumberLoginLogic(test_data.sign_phone[0])
    print(test_data.sign_phone[0])
    Logic.merchant.confirmMerchant()
    Logic.merchant.passGuidePage()
    Logic.common.recordPassResult(('//main/div/section/section[3]/p'), '매출정산','login', 2, 3)
    Logic.merchant.resign()
except Exception as e:
    Logic.common.recordFailResult(('//main/div/section/section[3]/p'), '매출정산','login', 2, 3)
    pass

webDriver.wd.quit()