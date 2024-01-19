from configuration import webDriver
import controlImage.compareImage as compareImage
import signUp

webDriver.cal()

signUp.merchant()
signUp.phoneNumberLoginclick()
signUp.phoneNumberLoginLogic()

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