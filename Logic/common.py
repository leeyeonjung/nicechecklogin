from configuration import webDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import utilities.ExcelUtils
from datetime import datetime
import time

file_path = './/testData//data.xlsx'

context_handles = webDriver.wd.contexts
# webDriver.wd.switch_to.context(context_handles[0]) native / webDriver.wd.switch_to.context('WEBVIEW_kr.co.nicevan.bujaapp') webview

#휴대폰 번호로 회원가입 진입
def phoneNumberLoginclick():
    webDriver.xpath('//main/div[2]/div[3]/div/button[1]').click()
    time.sleep(1.0)
    
#휴대폰 번호로 회원가입
def phoneNumberLoginLogic(sign_phone):

    name=sign_phone[0]
    email=sign_phone[1]
    phonenumber=str(sign_phone[2])

    webDriver.xpath('//input[@name="name"]').send_keys(name)
    time.sleep(0.5)
    webDriver.xpath('/html/body/main/div[2]/div[2]/button[1]').click()
    time.sleep(0.5)

    webDriver.xpath('//input[@name="email"]').send_keys(email)
    time.sleep(0.5)
    webDriver.xpath('/html/body/main/div[2]/div[2]/button[1]').click()
    time.sleep(0.5)

    webDriver.xpath('//input[@name="phone"]').send_keys(phonenumber)
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
def kakaoLoginLogic(sign_kakao):
    email=sign_kakao[0]
    password=sign_kakao[1]

    #단말기에 카카오앱 미설치 상태로 3초 wait 후, kakao element 확인되면 이메일, 비밀번호 입력하여 로그인
    try:
        WebDriverWait(webDriver.wd, 3).until(EC.presence_of_element_located((By.XPATH, '//h1/span/span')))
        #아이디 입력
        webDriver.xpath('//input[@name="loginId"]').send_keys(email)
        time.sleep(0.5)
        #비밀번호 입력
        webDriver.xpath('//input[@name="password"]').send_keys(password)
        time.sleep(0.5)
        #로그인 버튼 클릭
        webDriver.xpath('//article[@id="mainContent"]/div/div/form/div[4]/button').click()
        time.sleep(2.0)
    #단말에 카카오앱 설치 상태로 kakao 웹페이지 element 확인 되지 않으면 이메일, 비밀번호 입력 절차 pass
    except Exception:
        pass

    time.sleep(1.0)

def recordResult(result1, result2, tc, rownum, columnnum):
    if WebDriverWait(webDriver.wd, 3).until(EC.presence_of_element_located((By.XPATH, result1))) == result2:
         utilities.ExcelUtils.writeData(file_path,'result', rownum, columnnum, (tc + ' pass ' + (datetime.now().strftime("%Y-%m-%d %H:%M:%S"))))
    else:
         utilities.ExcelUtils.writeData(file_path,'result', rownum, columnnum, (tc + ' fail ' + (datetime.now().strftime("%Y-%m-%d %H:%M:%S"))))
