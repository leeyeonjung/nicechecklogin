from configuration import webDriver
import utilities.ExcelUtils as ExcelUtils
from selenium.webdriver.common.by import By

file_path = './/testData//data.xlsx'  # 수정필요  #함수확인 필요
N = ExcelUtils.getRowCount(file_path, 'Sheet1')
wd = webDriver.cal()

for i in range(2, N+1):
    first = ExcelUtils.readData(file_path,'Sheet1',i,2)
    second = ExcelUtils.readData(file_path,'Sheet1',i,5)
    op= ExcelUtils.readData(file_path,'Sheet1',i,4)
    result = ExcelUtils.readData(file_path,'Sheet1',i,6)

    cal_result = (((wd.find_element(By.ID, value=('com.sec.android.app.popupcalculator:id/calc_edt_formula'))).text).split(' '))[0]

    if result == float(cal_result):
        print(f"TEST{i-1} : PASS")
    else:
        print(f"TEST{i-1} : FAIL")

        

