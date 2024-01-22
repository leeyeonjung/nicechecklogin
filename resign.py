from configuration import webDriver
from selenium.webdriver import ActionChains
import time

context_handles = webDriver.wd.contexts
# webDriver.wd.switch_to.context(context_handles[0]) native / webDriver.wd.switch_to.context(context_handles[1]) webview

def merchant():
    webDriver.wd.switch_to.context(context_handles[1])
    time.sleep(0.5)

    #마이페이지 진입
    webDriver.xpath('//header/div/a/img').click()
    time.sleep(0.5)

    #회원정보 진입
    webDriver.xpath('//section/div[2]/a[1]').click()
    time.sleep(0.5)

    some_tag = webDriver.xpath('//ul/li[5]')

    # somthing element 까지 스크롤
    action = ActionChains(webDriver.wd)
    action.move_to_element(some_tag).perform()

    webDriver.xpath('//main/div[3]/div[3]').click()
    #회원탈퇴
    webDriver.xpath('//ul/li[5]').click()
    time.sleep(0.5)

    #탈퇴사유 입력란
    webDriver.xpath('//textarea').send_keys('test')
    time.sleep(0.5)

    #안할래요
    # //div[@id="expired-modal"]/div/div/button[1]

    #탈퇴하기
    webDriver.xpath('//div[@id="expired-modal"]/div/div/button[2]').click()
    time.sleep(0.5)

    print('agency resign finished!')

def agency():
    webDriver.wd.switch_to.context(context_handles[1])

    #마이페이지 진입
    webDriver.xpath('//header/div/a[2]/img').click()

    #회원정보 진입
    webDriver.xpath('//section/div[2]/a').click()

    #회원탈퇴
    webDriver.xpath('//ul/li[5]').click()

    #탈퇴사유 입력란
    webDriver.xpath('//textarea').send_keys('test')

    #안할래요
    # //div[@id="expired-modal"]/div/div/button[1]

    #탈퇴하기
    webDriver.xpath('//div[@id="expired-modal"]/div/div/button[2]').click()

    print('agency resign finished!')