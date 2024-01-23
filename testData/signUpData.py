import utilities.ExcelUtils as ExcelUtils

file_path = './/testData//data.xlsx'

data=['sign_phone','sign_kakao','merchant_biz_no','agency_biz_no']

sign_phone = [(ExcelUtils.readData(file_path,data[0],2,i+2)) for i in range(4)]

sign_kakao = [(ExcelUtils.readData(file_path,data[1],2,i+2)) for i in range(4)]

merchant_biz_no = [(ExcelUtils.readData(file_path,data[2],2,i+2)) for i in range(4)]

agency_biz_no = [(ExcelUtils.readData(file_path,data[3],2,i+2)) for i in range(4)]
