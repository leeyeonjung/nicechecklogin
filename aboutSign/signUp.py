from configuration import webDriver
import controlImage.compareImage as compareImage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

context_handles = webDriver.wd.contexts
# webDriver.wd.switch_to.context(context_handles[0]) native / webDriver.wd.switch_to.context(context_handles[1]) webview

#가맹점 선택
def merchant():
    webDriver.wd.switch_to.context(context_handles[1])
    webDriver.xpath('//main/div[2]/div[2]/div/div[1]').click()
    time.sleep(0.3)

#대리점 선택
def agency():
    webDriver.wd.switch_to.context(context_handles[1])
    webDriver.xpath('//main/div[2]/div[2]/div/div[2]').click()
    time.sleep(0.3)

#휴대폰 번호로 회원가입 진입
def phoneNumberLoginclick():
    webDriver.xpath('//main/div[2]/div[3]/div/button[1]').click()
    time.sleep(1.0)
    
#휴대폰 번호로 회원가입
def phoneNumberLoginLogic():
    webDriver.xpath('//input[@name="name"]').send_keys("이연정")
    time.sleep(0.5)
    webDriver.xpath('/html/body/main/div[2]/div[2]/button[1]').click()
    time.sleep(0.5)

    webDriver.xpath('//input[@name="email"]').send_keys("asa4828@daum.net")
    time.sleep(0.5)
    webDriver.xpath('/html/body/main/div[2]/div[2]/button[1]').click()
    time.sleep(0.5)

    webDriver.xpath('//input[@name="phone"]').send_keys("01041729247")
    time.sleep(0.5)
    webDriver.xpath('/html/body/main/div[2]/div[2]/button[4]').click()
    time.sleep(0.5)

    #인증번호 전송 소요 대기로 인해 해당 로직에서만 time.sleep(3.0)
    webDriver.xpath('//div[@id="successPhoneAlert"]/div/div/button').click()
    time.sleep(3.0)

    #휴대폰 인증번호 자동으로 불러오기
    #정규식과 외부프로세서 실행을 통해 sms 메세지 값에서 인증번호 6자리만 저장하기
    import re
    import subprocess
    
    def get_sms():
        result = subprocess.run(['adb', 'shell', 'content', 'query', '--uri', 'content://sms/inbox', '--projection', 'address,body'], capture_output=True)
        
        # 결과가 정상적으로 반환되었을 때만 처리
        if result.returncode == 0:
            # bytes 형식으로 표준 출력을 가져온 후 utf-8로 디코딩
            stdout_text = result.stdout.decode('utf-8')
            print(stdout_text)

            # 개행 문자 기준으로 문자열 분리
            sms_list = stdout_text.splitlines()
            print(sms_list)

            #정규식을 이용해 인증번호 6자리 리턴
            for sms in sms_list:
                match = re.search(r'인증번호\[(\d{6})\]', sms)
                if match:
                    verification_code = match.group(1)
                    return verification_code

    # 가져온 SMS 출력
    sms_code = get_sms()
    time.sleep(0.5)

    #인증번호 입력란에 번호 입력
    webDriver.xpath('//input[@name="authNum"]').send_keys(sms_code)
    time.sleep(0.5)

    #다음 버튼 선택
    webDriver.xpath('/html/body/main/div[2]/div[2]/button[5]').click()
    time.sleep(0.5)

    #가입하기 버튼 선택
    webDriver.xpath('/html/body/main/div[2]/div[2]/button[3]').click()

    #서비스 약관 동의
    #전체동의
    webDriver.xpath('//main/div[2]/div[1]/div/div[1]/label').click()
    #약관1동의
    #//main/div[2]/div[1]/div/div[2]/label
    #약관2동의
    #//main/div[2]/div[1]/div/div[3]/label
    #전표몰 동의
    #//main/div[2]/div[1]/div/div[4]/label
    time.sleep(0.5)

    webDriver.xpath('//button').click()
    time.sleep(1.0)

#카카오 회원가입 화면 진입
def kakaoLoginClick():
    webDriver.xpath('//main/div[2]/div[3]/div/button[2]').click()
    time.sleep(2.0)

#카카오로 회원가입 로직
def kakaoLoginLogic():

    #단말기에 카카오앱 미설치 상태로 3초 wait 후, kakao element 확인되면 이메일, 비밀번호 입력하여 로그인
    try:
        WebDriverWait(webDriver.wd, 3).until(EC.presence_of_element_located((By.XPATH, '//h1/span/span')))
        #아이디 입력
        webDriver.xpath('//input[@name="loginId"]').send_keys('asa4828@daum.net')
        time.sleep(0.5)
        #비밀번호 입력
        webDriver.xpath('//input[@name="password"]').send_keys('jeong0109**')
        time.sleep(0.5)
        #로그인 버튼 클릭
        webDriver.xpath('//article[@id="mainContent"]/div/div/form/div[4]/button').click()
        time.sleep(2.0)
    #단말에 카카오앱 설치 상태로 kakao 웹페이지 element 확인 되지 않으면 이메일, 비밀번호 입력 절차 pass
    except Exception:
        pass

    time.sleep(1.0)

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

#대리점 인증 화면
def confirmAgency():
    webDriver.xpath('//input[@name="biz-no"]').click()
    time.sleep(0.5)

    #대리점 사업자번호, 대리점 번호 입력
    agency_num=['4110391871','8405']

    #send_keys를 이용하여 내용 입력시, javascript 사업자번호 10자리로 인식 불가로 해당로직 press_keycode로 구현

    #대리점 사업자 번호
    for i in agency_num[0]:
        webDriver.wd.press_keycode(int(i)+7) #1
        time.sleep(0.3)
    time.sleep(1.0)

    #대리점 코드
    webDriver.xpath('//input[@name="code"]').click()

    for i in agency_num[1]:
        webDriver.wd.press_keycode(int(i)+7) #1
        time.sleep(0.3)
    time.sleep(1.0)

    webDriver.xpath('//button').click()
    time.sleep(1.0)