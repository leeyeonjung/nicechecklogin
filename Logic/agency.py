from configuration import webDriver
import time

context_handles = webDriver.wd.contexts
# webDriver.wd.switch_to.context(context_handles[0]) native / webDriver.wd.switch_to.context(context_handles[1]) webview

#대리점 선택
def intoAgency():
    webDriver.wd.switch_to.context(context_handles[1])
    webDriver.xpath('//main/div[2]/div[2]/div/div[2]').click()
    time.sleep(0.3)

#대리점 인증 화면
def confirmAgency(agency_biz_no):
    webDriver.xpath('//input[@name="biz-no"]').click()
    time.sleep(0.5)

    #대리점 사업자번호, 대리점 번호 입력
    agency_num=agency_biz_no

    #send_keys를 이용하여 내용 입력시, javascript 사업자번호 10자리로 인식 불가로 해당로직 press_keycode로 구현

    #대리점 사업자 번호
    for i in str(agency_num[0]):
        webDriver.wd.press_keycode(int(i)+7) #1
        time.sleep(0.3)
    time.sleep(1.0)

    #대리점 코드
    webDriver.xpath('//input[@name="code"]').click()

    for i in str(agency_num[1]):
        webDriver.wd.press_keycode(int(i)+7) #1
        time.sleep(0.3)
    time.sleep(1.0)

    webDriver.xpath('//button').click()
    time.sleep(3.0)

def resign():

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