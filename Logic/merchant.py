from configuration import webDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from controlImage import compareImage
import time



context_handles = webDriver.wd.contexts
print(context_handles)
# webDriver.wd.switch_to.context(context_handles[0]) native / webDriver.wd.switch_to.context(context_handles[1]) webview

#가맹점 선택
def intoMerchant():
    webDriver.wd.switch_to.context(context_handles[1])
    webDriver.xpath('//main/div[2]/div[2]/div/div[1]').click()
    time.sleep(0.3)

#가이드화면 넘기기
def passGuidePage():

    #기존 저장된 가이드 화면과 유사도 판정 후, 가이드 화면과 동일한 내용으로 확인 되면 화면 클릭 2번과 시작하기 버튼 눌러서 가이드 넘기기
    #비교군 이미지 경로
    guideImage = 'C:/mobile_automation_testing/niceCheck/niceCheck_Login/controlImage/image/guide.png'

    #스크린샷 이미지 경로
    screenshotImage = 'C:/mobile_automation_testing/niceCheck/niceCheck_Login/controlImage/image/screenshot.png'
    #이미지 스크린샷 저장
    webDriver.wd.save_screenshot(screenshotImage)

    #스크린샷 사이즈 crop 경로
    cropScreenshotImage='C:/mobile_automation_testing/niceCheck/niceCheck_Login/controlImage/image/cropScreenShot.png'
    #스크린샷 사이즈 변경
    compareImage.cropImage(screenshotImage,cropScreenshotImage)

    #이미지 비교 및 결과를 result에 저장
    result = compareImage.compare(guideImage, cropScreenshotImage)
    print(result)

    #유사도가 사전 설정된 임계값 이상이면 pass를 반환 / 미만이면 fail 반환
    #result가 pass이면 가이드 화면 클릭하여 넘기기

    if result >= 90:
        for i in range(2):
            webDriver.wd.swipe(300, 100, 100, 100)
            time.sleep(0.5)
        webDriver.xpath('//button').click()
    #가이드 화면이 뜨지 않는다면 pass
    else:
        pass

#사업자 미등록 가맹점 로직
def confirmMerchant():
    try:
        WebDriverWait(webDriver.wd, 3).until(EC.presence_of_element_located((By.XPATH, '//div[@id="successJoinAlert"]')))
        webDriver.xpath('//div[@id="successJoinAlert"]/div/div/button').click()
    except Exception:
        pass
    time.sleep(1.0)

def resign():
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