from appium import webdriver
from selenium.webdriver.common.by import By

desired_cap = {
  "appium:deviceName": "R3CR702LQGV",
  "platformName": "android",
  "appium:appPackage": "kr.co.nicevan.bujaapp",
  "appium:appActivity": "kr.co.nicevan.bujaapp.MainActivity",
  # "autoWebview" : "true", #자동 웹뷰 열기
  # "noReset" : "true", #App data no reset
  "autoGrantPermissions": "true" #권한 전체 자동 허용
}

wd = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)

def cal():
  wd.implicitly_wait(5)
  return wd

def xpath(data):
  return wd.find_element(By.XPATH, data)

def id(data):
  return wd.find_element(By.ID, data)

    
# ['NATIVE_APP', 'WEBVIEW_kr.co.nicevan.bujaapp']