from appium import webdriver
from selenium.webdriver.common.by import By
<<<<<<< HEAD
from appium.options.android import UiAutomator2Options

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Android',
    appPackage="kr.co.nicevan.bujaapp",
    appActivity='kr.co.nicevan.bujaapp.MainActivity',
    autoWebview="true", #자동 웹뷰 열기
    # noReset="true", #App data no reset
    autoGrantPermissions="true" #권한 전체 자동 허용
)

appium_server_url = 'http://localhost:4723'

wd = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

def cal():
  wd.implicitly_wait(5)
  return wd
=======

desired_cap = {
  "appium:deviceName": "R5CR807WVEJ",
  "platformName": "android",
  "appium:appPackage": "kr.co.nicevan.bujaapp",
  "appium:appActivity": "kr.co.nicevan.bujaapp.MainActivity",
  "autoWebview" : "true", #자동 웹뷰 열기
  # "noReset" : "true", #App data no reset
  "autoGrantPermissions": "true" #권한 전체 자동 허용
}

wd = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
>>>>>>> 6227792b190c42e077bd02640c56f86496c7f3a5

def cal():
  wd.implicitly_wait(5)
  return wd

def xpath(data):
  return wd.find_element(By.XPATH, data)

def id(data):
  return wd.find_element(By.ID, data)

    
#webDriver.wd.close_app() / 앱 종료
#webDriver.wd.launch_app() / 앱 백그라운드에서 재시작
#webDriver.wd.reset() 
# ['NATIVE_APP', 'WEBVIEW_kr.co.nicevan.bujaapp']