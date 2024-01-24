import Logic.common
import Logic.merchant
import test_data
from configuration import webDriver

webDriver.cal()

Logic.merchant.intoMerchant()
Logic.common.kakaoLoginClick()
#sign_kakao(email, password)
Logic.common.kakaoLoginLogic(test_data.sign_kakao[0])
print(test_data.sign_kakao[0])
Logic.merchant.confirmMerchant()
Logic.merchant.passGuidePage()
Logic.merchant.resign()

webDriver.wd.close_app()
webDriver.wd.launch_app()

Logic.merchant.intoMerchant()
Logic.common.phoneNumberLoginclick()
#sign_phone(name, email, phonenumber)
Logic.common.phoneNumberLoginLogic(test_data.sign_phone[0])
print(test_data.sign_phone[0])
Logic.merchant.confirmMerchant()
Logic.merchant.passGuidePage()
Logic.merchant.resign()

webDriver.wd.quit()