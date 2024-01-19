from configuration import webDriver
import controlImage.compareImage as compareImage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import signUp

webDriver.cal()

signUp.merchant()
signUp.kakaoLoginClick()

try:
    element = WebDriverWait(webDriver.wd, 3).until(EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="Kakao"]')))
    signUp.kakaoLoginLogic()
except Exception:
    pass

screenshotImage = 'C:/mobile_automation_testing/niceCheck/niceCheck_Login/controlImage/image/screenshot.png'
webDriver.wd.save_screenshot(screenshotImage)
compareImage.cropImage(screenshotImage)
splashImage = 'C:/mobile_automation_testing/niceCheck/niceCheck_Login/controlImage/image/splash.png'
cropScreenshotImage='C:/mobile_automation_testing/niceCheck/niceCheck_Login/controlImage/image/cropScreenShot.png'
# 이미지 비교 및 결과 출력
result = compareImage.imageSimilarity(splashImage, cropScreenshotImage)
print(result)

if result == 'pass':
    signUp.passGuidePage()
else:
    pass

signUp.passorfail()