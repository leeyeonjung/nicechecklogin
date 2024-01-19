from configuration import webDriver
import time

webDriver.cal()

context_handles = webDriver.wd.contexts

# webDriver.wd.switch_to.context(context_handles[0]) native
# webDriver.wd.switch_to.context(context_handles[1]) webview

#가맹점 선택
def merchant():
    webDriver.xpath('//android.widget.TextView[@text="가맹점"]').click()
    time.sleep(0.3)

#대리점 선택
def agency():
    webDriver.xpath('//android.widget.TextView[@text="나이스대리점"]').click()
    time.sleep(0.3)

#카카오 회원가입 클릭
def phoneNumberLoginclick():
    webDriver.wd.switch_to.context(context_handles[0])
    webDriver.xpath('//android.widget.Button[@text="휴대폰번호로 회원가입"]').click()
    time.sleep(2.0)
    
#휴대폰 번호로 회원가입
def phoneNumberLoginLogic():
    webDriver.wd.switch_to.context(context_handles[1])

    webDriver.xpath('//main/div[2]/div[3]/div/button[1]/img').click()
    time.sleep(1.0)

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

    webDriver.xpath('//div[@id="successPhoneAlert"]/div/div/button').click()
    time.sleep(3.0)

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

            for sms in sms_list:
                match = re.search(r'인증번호\[(\d{6})\]', sms)
                if match:
                    verification_code = match.group(1)
                    return verification_code

    # 가져온 SMS 출력
    sms_code = get_sms()
    time.sleep(0.5)

    #인증번호 입력
    webDriver.xpath('//input[@name="authNum"]').send_keys(sms_code)
    time.sleep(0.5)

    #다음 버튼 선택
    webDriver.xpath('/html/body/main/div[2]/div[2]/button[5]').click()
    time.sleep(0.5)

    #가입하기 버튼 선택
    webDriver.xpath('/html/body/main/div[2]/div[2]/button[3]').click()

    webDriver.wd.switch_to.context(context_handles[0])
    #서비스 약관 동의
    #전체동의
    webDriver.xpath('//android.widget.TextView[@text="전체 동의"]').click()
    #약관1동의
    #//android.webkit.WebView[@text="NICE CHECK APP"]/android.view.View/android.view.View[2]/android.view.View[2]
    #약관2동의
    #//android.webkit.WebView[@text="NICE CHECK APP"]/android.view.View/android.view.View[2]/android.view.View[3]
    #약관3동의
    #//android.webkit.WebView[@text="NICE CHECK APP"]/android.view.View/android.view.View[2]/android.view.View[4]
    time.sleep(0.5)

    webDriver.xpath('//android.widget.Button[@text="시작하기"]').click()
    time.sleep(1.0)

#카카오 회원가입 클릭
def kakaoLoginClick():
    webDriver.xpath('//android.widget.Button[@text="카카오로 회원가입"]').click()
    time.sleep(2.0)

def kakaoLoginLogic():
    webDriver.wd.switch_to.context(context_handles[1])
    #아이디 입력
    webDriver.xpath('//input[@name="loginId"]').send_keys('asa4828@daum.net')
    time.sleep(0.5)
    #비밀번호 입력
    webDriver.xpath('//input[@name="password"]').send_keys('jeong0109**')
    time.sleep(0.5)
    #로그인 버튼 클릭
    webDriver.xpath('//article[@id="mainContent"]/div/div/form/div[4]/button').click()
    time.sleep(2.0)

#대리점인증화면
def confirmAgency():
    webDriver.wd.switch_to.context(context_handles[0])

    #대리점 번호
    agency_num='411391871'

    # 대상 엘리먼트 선택
    input_element = webDriver.xpath('//android.webkit.WebView[@text="NICE CHECK APP"]/android.view.View/android.view.View[2]/android.widget.EditText[1]')

    # 기존 텍스트 먼저 입력
    input_element.send_keys(agency_num[0])

    # 나머지 텍스트를 1글자씩 추가하면서 0.1초 간격으로 대기
    for char in agency_num[1:]:
        time.sleep(0.1)
        input_element.send_keys(char)

    time.sleep(0.5)
    #대리점 코드
    webDriver.xpath('//android.webkit.WebView[@text="NICE CHECK APP"]/android.view.View/android.view.View[2]/android.widget.EditText[2]').send_keys('8405')
    time.sleep(0.5)
    #대표,점장,매니저 선택란
    # //android.webkit.WebView[@text="NICE CHECK APP"]/android.view.View/android.view.View[2]/android.view.View[1]
    # //android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="대표"]
    # //android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="점장"]
    # //android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="매니저"]

    webDriver.xpath('//android.widget.Button[@text="완료"]').click()
    time.sleep(1.0)

#가이드화면 넘기기
def passGuidePage():
    webDriver.wd.switch_to.context(context_handles[0])
    webDriver.xpath('//android.webkit.WebView[@text="NICE CHECK APP"]/android.view.View/android.view.View/android.widget.TextView').click()
    time.sleep(0.5)
    webDriver.xpath('//android.webkit.WebView[@text="NICE CHECK APP"]/android.view.View/android.view.View/android.widget.TextView').click()
    time.sleep(0.5)
    webDriver.wd.switch_to.context(context_handles[1])
    webDriver.xpath('//button').click()

#pass의 기준
def passorfail():
    webDriver.wd.switch_to.context(context_handles[0])
    if (((webDriver.id('totalAmount')).text) == '실시간 매출'):
        print('login pass')
    else:
        print ('login fail')