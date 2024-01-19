from configuration import webDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import signUp

webDriver.cal()

signUp.agency()

signUp.kakaoLoginClick()

try:
    element = WebDriverWait(webDriver.wd, 3).until(EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="Kakao"]')))
    signUp.kakaoLoginLogic()
except Exception:
    pass

signUp.confirmAgency()

signUp.passorfail()
