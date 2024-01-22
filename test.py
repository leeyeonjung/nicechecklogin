from configuration import webDriver
from selenium.webdriver import ActionChains
import time

webDriver.cal()

context_handles = webDriver.wd.contexts

webDriver.wd.switch_to.context(context_handles[1])
time.sleep(0.5)

#마이페이지 진입
webDriver.xpath('//header/div/a/img').click()
time.sleep(0.5)

#회원정보 진입
webDriver.xpath('//section/div[2]/a[1]').click()
time.sleep(0.5)

webDriver.wd.switch_to.context(context_handles[0])

element = webDriver.xpath('//android.view.View[@text="회원 탈퇴"]')


#회원탈퇴
element.click()
# time.sleep(0.5)

# #탈퇴사유 입력란
# webDriver.xpath('//textarea').send_keys('test')
# time.sleep(0.5)

# #안할래요
# # //div[@id="expired-modal"]/div/div/button[1]

# #탈퇴하기
# webDriver.xpath('//div[@id="expired-modal"]/div/div/button[2]').click()
# time.sleep(0.5)

# print('agency resign finished!')