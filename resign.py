from configuration import webDriver
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

    #회원 탈퇴 버튼 뜨게 스크롤링
    webDriver.wd.swipe(100, 500, 100, 100, 1500)
    time.sleep(0.5)

    #탈퇴 모달 팝업 선택
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

    print('merchant resign finished!')
    time.sleep(2.0)
    
def agency():
    webDriver.wd.switch_to.context(context_handles[1])

    #마이페이지 진입
    webDriver.xpath('//header/div/a[2]/img').click()

    #회원정보 진입
    webDriver.xpath('//section/div[2]/a').click()

    #회원 탈퇴 버튼 뜨게 스크롤링
    webDriver.wd.swipe(100, 500, 100, 100)
    time.sleep(0.5)

    #회원탈퇴
    webDriver.xpath('//ul/li[5]').click()

    #탈퇴사유 입력란
    webDriver.xpath('//textarea').send_keys('test')

    #안할래요
    # //div[@id="expired-modal"]/div/div/button[1]

    #탈퇴하기
    webDriver.xpath('//div[@id="expired-modal"]/div/div/button[2]').click()

    print('agency resign finished!')
    time.sleep(2.0)